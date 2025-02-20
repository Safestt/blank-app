import streamlit as st

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
    st.write("Aquí iría el formulario de registro")
   
    username = st.text_input("Usuario", placeholder="Ingrese un usuario para registrarse")
    
    password = st.text_input("Contraseña", type="password", placeholder="Ingrese su contraseña")
    password_confirmation = st.text_input("Contraseña confirmacion", type="password", placeholder="Ingrese su contraseña nuevamente")
    
    if st.button("Registrarse"):
        #Logica para autenticacion
        st.write("Coming soon")
    if st.button("Volver al inicio"):
        st.session_state.page = "home"
