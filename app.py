import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Proyecto Python Fundamentals",
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


# ==========================
# HOME
# ==========================

if opcion == "Home":

    st.title("Proyecto Python Fundamentals")

    st.subheader("Especialización en Python for Analytics")

    st.write("Proyecto práctico del Módulo 1 - Python Fundamentals")

    st.write(
        "En este proyecto se aplican conceptos fundamentales de Python, "
        "estructuras de datos, NumPy, Pandas, funciones, clases y Streamlit."
    )

    st.markdown("""
    ### Tecnologías utilizadas

    - Python
    - Streamlit
    - NumPy
    - Pandas
    """)


# ==========================
# EJERCICIO 1
# ==========================

elif opcion == "Ejercicio 1":

    st.title("Ejercicio 1 - Flujo de Caja")

    st.write(
        "Registra los movimientos de caja indicando el concepto, "
        "tipo de movimiento y valor."
    )

    # Crear la lista de movimientos
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    st.subheader("Registrar movimiento")

    concepto = st.text_input(
        "Concepto",
        placeholder="Ejemplo: Venta de productos"
    )

    tipo = st.selectbox(
        "Tipo de movimiento",
        ["Ingreso", "Gasto"]
    )

    valor = st.number_input(
        "Valor",
        min_value=0.0,
        step=0.01
    )

    if st.button("Agregar movimiento"):

        if concepto == "":
            st.warning("Ingrese un concepto.")

        elif valor <= 0:
            st.warning("Ingrese un valor mayor a 0.")

        else:

            movimiento = {
                "concepto": concepto,
                "tipo": tipo,
                "valor": valor
            }

            st.session_state.movimientos.append(movimiento)

            st.success("Movimiento agregado correctamente.")

    st.subheader("Movimientos registrados")

    if len(st.session_state.movimientos) > 0:

        for movimiento in st.session_state.movimientos:

            st.write(
                f"**{movimiento['concepto']}** | "
                f"{movimiento['tipo']} | "
                f"S/ {movimiento['valor']:.2f}"
            )

    else:

        st.info("Todavía no hay movimientos registrados.")

    # Calcular totales
    total_ingresos = 0
    total_gastos = 0

    for movimiento in st.session_state.movimientos:

        if movimiento["tipo"] == "Ingreso":
            total_ingresos += movimiento["valor"]

        elif movimiento["tipo"] == "Gasto":
            total_gastos += movimiento["valor"]

    saldo = total_ingresos - total_gastos

    # Mostrar resumen
    st.subheader("Resumen del flujo de caja")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total ingresos",
        f"S/ {total_ingresos:,.2f}"
    )

    col2.metric(
        "Total gastos",
        f"S/ {total_gastos:,.2f}"
    )

    col3.metric(
        "Saldo",
        f"S/ {saldo:,.2f}"
    )
elif opcion == "Ejercicio 2":

    st.title("Ejercicio 2 - Registro de Productos")

    st.write(
        "Registra productos utilizando arrays de NumPy "
        "y convierte la información en un DataFrame."
    )

    # Crear los arrays en session_state
    if "productos" not in st.session_state:
        st.session_state.productos = np.array([], dtype=object)

    if "categorias" not in st.session_state:
        st.session_state.categorias = np.array([], dtype=object)

    if "precios" not in st.session_state:
        st.session_state.precios = np.array([], dtype=float)

    if "cantidades" not in st.session_state:
        st.session_state.cantidades = np.array([], dtype=int)

    # Formulario
    st.subheader("Registrar producto")

    producto = st.text_input(
        "Nombre del producto",
        placeholder="Ejemplo: Laptop"
    )

    categoria = st.selectbox(
        "Categoría",
        ["Tecnología", "Oficina", "Accesorios", "Otros"]
    )

    precio = st.number_input(
        "Precio unitario",
        min_value=0.0,
        step=0.01
    )

    cantidad = st.number_input(
        "Cantidad",
        min_value=1,
        step=1
    )

    if st.button("Agregar producto"):

        if producto == "":
            st.warning("Ingrese el nombre del producto.")

        elif precio <= 0:
            st.warning("Ingrese un precio mayor a 0.")

        else:

            # Agregar datos a los arrays
            st.session_state.productos = np.append(
                st.session_state.productos,
                producto
            )

            st.session_state.categorias = np.append(
                st.session_state.categorias,
                categoria
            )

            st.session_state.precios = np.append(
                st.session_state.precios,
                precio
            )

            st.session_state.cantidades = np.append(
                st.session_state.cantidades,
                cantidad
            )

            st.success("Producto agregado correctamente.")

    # Mostrar información
    if len(st.session_state.productos) > 0:

        # Calcular total
        totales = (
            st.session_state.precios *
            st.session_state.cantidades
        )

        # Crear DataFrame
        df_productos = pd.DataFrame({
            "Producto": st.session_state.productos,
            "Categoría": st.session_state.categorias,
            "Precio": st.session_state.precios,
            "Cantidad": st.session_state.cantidades,
            "Total": totales
        })

        st.subheader("Productos registrados")

        st.dataframe(
            df_productos,
            use_container_width=True
        )

    else:

        st.info("Todavía no hay productos registrados.")
