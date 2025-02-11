import streamlit as st
import random
import string

st.set_page_config(page_title="Competencia de Código", layout="centered")

st.title("🏆 Competencia de Código en Tiempo Real")

# Sección de emparejamiento
modo = st.radio("¿Quieres crear una sala o unirte a una existente?", ["Crear", "Unirse"])

if "codigo_sala" not in st.session_state:
    st.session_state["codigo_sala"] = None

if modo == "Crear":
    if st.button("Generar Código de Invitación"):
        codigo_sala = "".join(random
