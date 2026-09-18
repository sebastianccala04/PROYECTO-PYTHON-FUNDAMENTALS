import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Proyecto Python Fundamentals",
    page_icon="🐍",
    layout="wide")

# Menú lateral
st.sidebar.title("Menú principal")

opcion = st.sidebar.selectbox(
    "Selecciona una sección:",
    ["Home",
    "Ejercicio 1",
    "Ejercicio 2",
    "Ejercicio 3",
    "Ejercicio 4"])
