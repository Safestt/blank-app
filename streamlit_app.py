import streamlit as st

st.title("Inicio de Sesión")

# Campos de entrada
usuario = st.text_input("Usuario", key="usuario")
password = st.text_input("Contraseña", type="password", key="password")

# Botón de login
if st.button("Iniciar Sesión"):
    st.write("Aquí iría la lógica de autenticación")
