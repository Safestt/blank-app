import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
import random
import string
import time

# Inicializar Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccount.json")
    firebase_admin.initialize_app(cred, {"databaseURL": "https://tu-proyecto.firebaseio.com"})

# Referencia a la base de datos
ref = db.reference("/salas")

st.title("Competencia de Código en Tiempo Real")

# Opción para crear o unirse a una sala
modo = st.radio("¿Quieres crear una sala o unirte a una existente?", ["Crear", "Unirse"])

if modo == "Crear":
    if st.button("Generar Código de Invitación"):
        codigo = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
        ref.child(codigo).set({"jugadores": 1})
        st.session_state["codigo_sala"] = codigo
        st.success(f"Comparte este código: {codigo}")

elif modo == "Unirse":
    codigo_sala = st.text_input("Ingresa el código de la sala:")
    if st.button("Unirme"):
        sala = ref.child(codigo_sala).get()
        if sala and sala["jugadores"] == 1:
            ref.child(codigo_sala).update({"jugadores": 2})
            st.session_state["codigo_sala"] = codigo_sala
            st.success("Te has unido a la sala.")
        else:
            st.error("Código inválido o sala llena.")

# Mostrar la interfaz solo si hay una sala activa
if "codigo_sala" in st.session_state:
    st.subheader(f"Sala: {st.session_state['codigo_sala']}")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Jugador 1")
        codigo_j1 = st.text_area("Código Jugador 1", height=200, key="j1")

    with col2:
        st.subheader("Jugador 2")
        codigo_j2 = st.text_area("Código Jugador 2", height=200, key="j2")

    st.code(codigo_j1, language="python")
    st.code(codigo_j2, language="python")
