import streamlit as st

def main():
    st.set_page_config(page_title="Login", page_icon="🔑", layout="centered")
    

    st.title("Iniciar Sesión")
    
    username = st.text_input("Usuario", placeholder="Ingrese su usuario")
    password = st.text_input("Contrassseña", type="password", placeholder="Ingrese su contraseña")
    
    if st.button("Ingresar"):
        st.success("Diseño cargado correctamente")
    
   
    
if __name__ == "__main__":
    main()
