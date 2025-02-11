import streamlit as st

st.title("Competencia de Código en Tiempo Real")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Jugador 1")
    codigo_jugador_1 = st.text_area("Código Jugador 1", height=200, key="j1")

with col2:
    st.subheader("Jugador 2")
    codigo_jugador_2 = st.text_area("Código Jugador 2", height=200, key="j2")

st.subheader("Código en Vivo")
st.code(codigo_jugador_1, language="python")
st.code(codigo_jugador_2, language="python")
