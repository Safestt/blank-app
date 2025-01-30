import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Saludo Python",
    page_icon="🐍",
    layout="centered"
)

# Inicializar la escena si no está definida
if "scene" not in st.session_state:
    st.session_state.scene = "inicio"

# Función para cambiar de escena
def change_scene(scene):
    st.session_state.scene = scene
    st.rerun()  # Forzar la actualización de la interfaz

# Escena de inicio
if st.session_state.scene == "inicio":
    st.title("¡Saludo al grupo de Python desde 0! 👋")
    st.success("🐍 Hola comunidad Python! 🚀")
    st.write("✨ Aprendiendo y creciendo juntos ✨")
    st.write("📚 🖥️ 🧠 💡")
    st.balloons()
    
    if st.button("Ir a escena 2"):
        change_scene("escena2")

# Segunda escena
elif st.session_state.scene == "escena2":
    st.title("Segunda Escena 🎭")
    st.write("¡Bienvenido a la segunda escena!")
    
    if st.button("Regresar al inicio"):
        change_scene("inicio")
