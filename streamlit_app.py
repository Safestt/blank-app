import streamlit as st
import requests
import time
Url_api = "https://api-test-0cxg.onrender.com/"

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
            st.rerun()
    with col2:
        if st.button("Registrarse"):
            st.session_state.page = "register"
            st.rerun()

# Página de Registro
elif st.session_state.page == "register":
    st.title("Registro")
   
    username = st.text_input("Usuario", placeholder="Ingrese un usuario para registrarse")
    password = st.text_input("Contraseña", type="password", placeholder="Ingrese su contraseña")
    password_confirmation = st.text_input("Contraseña confirmacion", type="password", placeholder="Ingrese su contraseña nuevamente")
    
    if st.button("Registrarse"):
        if password != password_confirmation:
            st.error("Las contraseñas no coinciden!")
        elif password == password_confirmation and password and not username:
             st.error("Por favor ingresa un nombre de usuario valido")
        elif password == password_confirmation and username:
            data = {"username": username, "password": password}
            
            # Enviar el POST a la API
            response = requests.post(Url_api + "auth/register", json=data)
            
            if response.status_code == 200:
                st.success("¡Usuario registrado correctamente!")
                time.sleep(3)
                st.session_state.page = "home"
                st.rerun()  
            else:
                st.error(f"Error al registrar usuario: {response.json().get('detail', 'Error desconocido')}")
            
    if st.button("Volver al inicio"):
        st.session_state.page = "home"
        st.rerun()

elif st.session_state.page == "login":
    st.title("login")
    username = st.text_input("Usuario", placeholder="Ingrese un usuario para registrarse")
    password = st.text_input("Contraseña", type="password", placeholder="Ingrese su contraseña")
    if st.button("Ingresar"):
        if not username or not password:
            st.error("Por favor ingresa tu usuario y contraseña.")
        else:
            # Preparar los datos para la solicitud POST
            data = {"username": username, "password": password}
            
         
            response = requests.post(Url_api + "auth/login", json=data)
            
            if response.status_code == 200:
                respuesta_json = response.json()  
                verificacion = respuesta_json.get("Verificacion", False)  # Obtener el valor de 'Verificacion'
                
                if verificacion:  # Si es True, iniciar sesión
                    st.success("¡Inicio de sesión exitoso!")
                    time.sleep(3)
                    st.session_state.page = "logged_in"
                    st.rerun()
                else:
                    st.error("Credenciales incorrectas")
            else:
                st.error("Error en la conexión con la API")
    
    if st.button("Volver al inicio"):
        st.session_state.page = "home"
        st.rerun()

elif st.session_state.page == "logged_in":
    image_url = "https://img.freepik.com/fotos-premium/candado-morado-contrasena-e-icono-aprobado-proteccion-datos-icono-acceso-privado-contrasena-acceso-seguridad-proteccion-privacidad-informacion-personal-concepto-seguridad-ilustracion-renderizado-3d_473922-903.jpg?w=740"
    
    st.image(image_url, caption="Logged in", use_container_width=True)
    st.write("Actualmente no hay funcionalidades")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Salir"):
            st.write("Saliendo...")
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)  
                progress_bar.progress(i + 1)  
            st.session_state.page = "home"
            st.rerun()  
