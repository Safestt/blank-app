import streamlit as st
import time

st.title("🏆 Competencia de Código")

# Crear variables en la sesión
if "sala" not in st.session_state:
    st.session_state["sala"] = None
    st.session_state["jugador1_listo"] = False
    st.session_state["jugador2_listo"] = False

# Auto-refresh cada 2 segundos (simula tiempo real)
st.session_state["refrescar"] = st.session_state.get("refrescar", 0)
st.session_state["refrescar"] += 1
time.sleep(2)  # Simula una actualización cada 2 segundos
st.rerun()  # Fuerza la actualización

modo = st.radio("¿Crear o Unirse a una sala?", ["Crear", "Unirse"])

if modo == "Crear":
    if st.button("Generar Código de Invitación"):
        st.session_state["sala"] = "SALA123"
        st.success(f"🔗 Comparte este código: `{st.session_state['sala']}`")

elif modo == "Unirse":
    sala_ingresada = st.text_input("Ingresa el código de la sala:")
    if st.button("Unirme"):
        if sala_ingresada == "SALA123":
            st.session_state["sala"] = sala_ingresada
            st.success(f"✅ Te has unido a la sala `{sala_ingresada}`")
        else:
            st.error("❌ Sala no encontrada")

if st.session_state["sala"]:
    st.subheader(f"Sala: `{st.session_state['sala']}`")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Estoy listo (Jugador 1)"):
            st.session_state["jugador1_listo"] = True

    with col2:
        if st.button("✅ Estoy listo (Jugador 2)"):
            st.session_state["jugador2_listo"] = True

    # Mostrar estado en tiempo real
    st.write("### Estado de los jugadores:")
    st.write(f"👤 Jugador 1: {'🟢 Listo' if st.session_state['jugador1_listo'] else '⏳ Esperando...'}")
    st.write(f"👤 Jugador 2: {'🟢 Listo' if st.session_state['jugador2_listo'] else '⏳ Esperando...'}")

    if st.session_state["jugador1_listo"] and st.session_state["jugador2_listo"]:
        st.success("🚀 ¡Ambos jugadores están listos!")
