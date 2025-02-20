import streamlit as st
import time

# Inicializar estado de la página si no existe
if "page" not in st.session_state:
    st.session_state.page = "home"

st.title("Demo 🚀")
# Página de Inicio
if st.session_state.page == "home":
    st.write("Bienvenido, selecciona una opción:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Iniciar Sesión"):
            st.session_state.page = "login"
    with col2:
        if st.button("Registrarse"):
            st.session_state.page = "register"

# Página de Registro
elif st.session_state.page == "register":
    st.title("Registro")
   
    username = st.text_input("Usuario", placeholder="Ingrese un usuario para registrarse")
    
    password = st.text_input("Contraseña", type="password", placeholder="Ingrese su contraseña")
    password_confirmation = st.text_input("Contraseña confirmacion", type="password", placeholder="Ingrese su contraseña nuevamente")
    
    if st.button("Registrarse"):
        if password != password_confirmation:
            st.error("Las contraseñas no coinciden!")
        elif password == password_confirmation and password and password_confirmation and not username:
             st.error("Por favor ingresa un nombre de usuario valido")
        elif password == password_confirmation and username:
            st.success("Registrado correctamente")
            st.session_state.page = "home"
            time.sleep(2)
            st.rerun()
            
            
    if st.button("Volver al inicio"):
        st.session_state.page = "home"
