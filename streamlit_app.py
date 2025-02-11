import streamlit as st

st.title("🏆 Competencia de Código")

# Crear una sesión única con un código de sala
if "sala" not in st.session_state:
    st.session_state["sala"] = None
    st.session_state["jugador1_listo"] = False
    st.session_state["jugador2_listo"] = False

modo = st.radio("¿Crear o Unirse a una sala?", ["Crear", "Unirse"])

if modo == "Crear":
    if st.button("Generar Código de Invitación"):
        st.session_state["sala"] = "SALA123"  # Puedes hacer que sea aleatorio si quieres
        st.success(f"🔗 Comparte este código: `{st.session_state['sala']}`")

elif modo == "Unirse":
    sala_ingresada = st.text_input("Ingresa el código de la sala:")
    if st.button("Unirme"):
        if sala_ingresada == "SALA123":  # Simulación sin servidor
            st.session_state["sala"] = sala_ingresada
            st.success(f"✅ Te has unido a la sala `{sala_ingresada}`")
        else:
            st.error("❌ Sala no encontrada")

if st.session_state["sala"]:
    st.subheader(f"Sala: `{st.session_state['sala']}`")

    # Botón para marcar como listo
    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Estoy listo (Jugador 1)"):
            st.session_state["jugador1_listo"] = True

    with col2:
        if st.button("✅ Estoy listo (Jugador 2)"):
            st.session_state["jugador2_listo"] = True

    # Mostrar estado de cada jugador
    st.write("### Estado de los jugadores:")
    st.write(f"👤 Jugador 1: {'🟢 Listo' if st.session_state['jugador1_listo'] else '⏳ Esperando...'}")
    st.write(f"👤 Jugador 2: {'🟢 Listo' if st.session_state['jugador2_listo'] else '⏳ Esperando...'}")

    # Si ambos están listos, mostrar mensaje final
    if st.session_state["jugador1_listo"] and st.session_state["jugador2_listo"]:
        st.success("🚀 ¡Ambos jugadores están listos!")
