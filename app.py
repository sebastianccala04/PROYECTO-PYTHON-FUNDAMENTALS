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

if opcion == "Home":

    st.title("Proyecto Python Fundamentals")

    st.subheader("Especialización en Python for Analytics")

    st.write("Proyecto práctico del Módulo 1 - Python Fundamentals")

    st.write("En este proyecto se aplican conceptos fundamentales de Python, "
             "estructuras de datos, NumPy, Pandas, funciones, clases y Streamlit.")

    st.markdown("""
    ### Tecnologías utilizadas

    - Python
    - Streamlit
    - NumPy
    - Pandas
    """)

if opcion == "Ejercicio 1":

    st.title("Ejercicio 1 - Flujo de Caja")

    st.write(
        "Registra los movimientos de caja indicando el concepto, "
        "tipo de movimiento y valor."
    )

    # Crear la lista de movimientos
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []
