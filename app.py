import streamlit as st
import numpy as np
import pandas as pd

# Librerías externas entregadas para el proyecto
from librería_funciones_proyecto1 import calcular_depreciacion_linea_recta
from librería_clases_proyecto1 import InventarioProducto


# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================

st.set_page_config(
    page_title="Proyecto 1 - Python Fundamentals",
    page_icon="🐍",
    layout="wide"
)


# =========================================================
# FUNCIONES AUXILIARES
# =========================================================

def inicializar_estado():
    """Inicializa los datos que deben conservarse durante la sesión."""

    # Ejercicio 1
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    # Ejercicio 2
    if "productos" not in st.session_state:
        st.session_state.productos = np.array([], dtype=object)

    if "categorias" not in st.session_state:
        st.session_state.categorias = np.array([], dtype=object)

    if "precios" not in st.session_state:
        st.session_state.precios = np.array([], dtype=float)

    if "cantidades" not in st.session_state:
        st.session_state.cantidades = np.array([], dtype=int)

    # Ejercicio 3
    if "historial_depreciacion" not in st.session_state:
        st.session_state.historial_depreciacion = []

    # Ejercicio 4
    if "inventario" not in st.session_state:
        st.session_state.inventario = []


def mostrar_moneda(valor):
    """Da formato monetario a un valor."""
    return f"S/ {valor:,.2f}"


inicializar_estado()


# =========================================================
# MENÚ LATERAL
# =========================================================

st.sidebar.title("🐍 Proyecto Python")

opcion = st.sidebar.selectbox(
    "Selecciona una sección:",
    [
        "Home",
        "Ejercicio 1",
        "Ejercicio 2",
        "Ejercicio 3",
        "Ejercicio 4"
    ]
)

st.sidebar.markdown("---")
st.sidebar.write("Python Fundamentals")
st.sidebar.write("Proyecto 1")


# =========================================================
# HOME
# =========================================================

if opcion == "Home":

    st.title("🐍 Proyecto Aplicado en Streamlit")
    st.subheader("Especialización en Python for Analytics")
    st.markdown("### Módulo 1 - Python Fundamentals")

    st.info(
        "Aplicación interactiva desarrollada para integrar los conceptos "
        "fundamentales aprendidos durante el módulo."
    )

    st.markdown("## Información del estudiante")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Nombre completo:** [Coloca aquí tu nombre completo]")
        st.write("**Curso:** Especialización Python for Analytics")
        st.write("**Módulo:** Python Fundamentals")

    with col2:
        st.write("**Proyecto:** Proyecto 1 - Aplicación en Streamlit")
        st.write("**Año:** 2026")
        st.write("**Tecnología principal:** Python + Streamlit")

    st.markdown("---")

    st.markdown("## Descripción del proyecto")

    st.write(
        "Esta aplicación integra estructuras de datos, widgets de Streamlit, "
        "NumPy, Pandas, funciones y programación orientada a objetos. "
        "Cada ejercicio presenta una solución interactiva y permite visualizar "
        "los resultados directamente en pantalla."
    )

    st.markdown("## Tecnologías utilizadas")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Lenguaje", "Python")
    col2.metric("Interfaz", "Streamlit")
    col3.metric("Arrays", "NumPy")
    col4.metric("Datos", "Pandas")


# =========================================================
# EJERCICIO 1 - FLUJO DE CAJA CON LISTAS
# =========================================================

elif opcion == "Ejercicio 1":

    st.title("💰 Ejercicio 1 - Flujo de Caja con Listas")

    st.markdown(
        """
        En este ejercicio se registran movimientos financieros utilizando
        una lista. Cada movimiento contiene un concepto, un tipo de movimiento
        y un valor. La aplicación calcula los ingresos, gastos y saldo final.
        """
    )

    st.subheader("Registrar movimiento")

    col1, col2, col3 = st.columns(3)

    with col1:
        concepto = st.text_input(
            "Concepto",
            placeholder="Ejemplo: Venta de productos"
        )

    with col2:
        tipo = st.selectbox(
            "Tipo de movimiento",
            ["Ingreso", "Gasto"]
        )

    with col3:
        valor = st.number_input(
            "Valor",
            min_value=0.0,
            step=0.01,
            format="%.2f"
        )

    if st.button("➕ Agregar movimiento", type="primary"):

        if concepto.strip() == "":
            st.warning("Ingrese un concepto.")

        elif valor <= 0:
            st.warning("El valor debe ser mayor que 0.")

        else:
            movimiento = {
                "concepto": concepto.strip(),
                "tipo": tipo,
                "valor": valor
            }

            st.session_state.movimientos.append(movimiento)

            st.success("Movimiento agregado correctamente.")

    st.markdown("---")
    st.subheader("Movimientos registrados")

    if st.session_state.movimientos:

        df_movimientos = pd.DataFrame(
            st.session_state.movimientos
        )

        df_movimientos["valor"] = df_movimientos["valor"].round(2)

        st.dataframe(
            df_movimientos,
            use_container_width=True,
            hide_index=True
        )

        total_ingresos = sum(
            movimiento["valor"]
            for movimiento in st.session_state.movimientos
            if movimiento["tipo"] == "Ingreso"
        )

        total_gastos = sum(
            movimiento["valor"]
            for movimiento in st.session_state.movimientos
            if movimiento["tipo"] == "Gasto"
        )

        saldo = total_ingresos - total_gastos

        st.subheader("Resumen del flujo de caja")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Total ingresos",
                mostrar_moneda(total_ingresos)
            )

        with col2:
            st.metric(
                "Total gastos",
                mostrar_moneda(total_gastos)
            )

        with col3:
            st.metric(
                "Saldo final",
                mostrar_moneda(saldo)
            )

        if saldo >= 0:
            st.success("El flujo de caja está a favor.")
        else:
            st.error("El flujo de caja está en contra.")

        if st.button("🗑️ Limpiar movimientos"):
            st.session_state.movimientos = []
            st.rerun()

    else:
        st.info("Todavía no hay movimientos registrados.")


# =========================================================
# EJERCICIO 2 - NUMPY + DATAFRAME
# =========================================================

elif opcion == "Ejercicio 2":

    st.title("📊 Ejercicio 2 - Registro con NumPy y DataFrame")

    st.markdown(
        """
        En este ejercicio se registran productos utilizando arreglos de NumPy.
        Posteriormente, los arrays se convierten en un DataFrame de Pandas
        para mostrar la información actualizada.
        """
    )

    st.subheader("Registrar producto")

    col1, col2 = st.columns(2)

    with col1:
        producto = st.text_input(
            "Nombre del producto",
            placeholder="Ejemplo: Laptop"
        )

        categoria = st.selectbox(
            "Categoría",
            [
                "Tecnología",
                "Oficina",
                "Accesorios",
                "Otros"
            ]
        )

    with col2:
        precio = st.number_input(
            "Precio unitario",
            min_value=0.0,
            step=0.01,
            format="%.2f"
        )

        cantidad = st.number_input(
            "Cantidad",
            min_value=1,
            step=1
        )

    if st.button("➕ Agregar producto", type="primary"):

        if producto.strip() == "":
            st.warning("Ingrese el nombre del producto.")

        elif precio <= 0:
            st.warning("El precio debe ser mayor que 0.")

        else:

            st.session_state.productos = np.append(
                st.session_state.productos,
                producto.strip()
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

    st.markdown("---")
    st.subheader("Productos registrados")

    if len(st.session_state.productos) > 0:

        # NumPy realiza la multiplicación elemento por elemento.
        totales = (
            st.session_state.precios
            * st.session_state.cantidades
        )

        # Conversión de los arrays a DataFrame.
        df_productos = pd.DataFrame({
            "Producto": st.session_state.productos,
            "Categoría": st.session_state.categorias,
            "Precio": st.session_state.precios,
            "Cantidad": st.session_state.cantidades,
            "Total": totales
        })

        st.dataframe(
            df_productos.style.format({
                "Precio": "S/ {:,.2f}",
                "Total": "S/ {:,.2f}"
            }),
            use_container_width=True,
            hide_index=True
        )

        total_ventas = float(totales.sum())

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Productos registrados",
                len(df_productos)
            )

        with col2:
            st.metric(
                "Valor total",
                mostrar_moneda(total_ventas)
            )

        if st.button("🗑️ Limpiar productos"):
            st.session_state.productos = np.array([], dtype=object)
            st.session_state.categorias = np.array([], dtype=object)
            st.session_state.precios = np.array([], dtype=float)
            st.session_state.cantidades = np.array([], dtype=int)
            st.rerun()

    else:
        st.info("Todavía no hay productos registrados.")


# =========================================================
# EJERCICIO 3 - FUNCIÓN DE LIBRERÍA EXTERNA
# =========================================================

elif opcion == "Ejercicio 3":

    st.title("🧮 Ejercicio 3 - Función desde Librería Externa")

    st.markdown(
        """
        En este ejercicio se utiliza una función de la librería externa
        `librería_funciones_proyecto1.py`.

        La función seleccionada está relacionada con contabilidad y permite
        calcular la depreciación de un activo mediante el método de línea recta.
        """
    )

    st.subheader("Función seleccionada")

    st.selectbox(
        "Selecciona la función:",
        ["calcular_depreciacion_linea_recta"]
    )

    st.write(
        "Fórmula: depreciación anual = "
        "(costo del activo - valor residual) / vida útil"
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        costo_activo = st.number_input(
            "Costo del activo",
            min_value=0.0,
            step=100.0,
            format="%.2f"
        )

    with col2:
        valor_residual = st.number_input(
            "Valor residual",
            min_value=0.0,
            step=100.0,
            format="%.2f"
        )

    with col3:
        vida_util = st.number_input(
            "Vida útil (años)",
            min_value=1,
            step=1
        )

    if st.button("▶️ Calcular depreciación", type="primary"):

        try:

            resultado = calcular_depreciacion_linea_recta(
                costo_activo,
                valor_residual,
                vida_util
            )

            st.success("Cálculo realizado correctamente.")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Depreciación anual",
                    mostrar_moneda(resultado["depreciacion_anual"])
                )

            with col2:
                st.metric(
                    "Depreciación mensual",
                    mostrar_moneda(resultado["depreciacion_mensual"])
                )

            registro = {
                "Costo activo": costo_activo,
                "Valor residual": valor_residual,
                "Vida útil (años)": vida_util,
                "Depreciación anual": resultado["depreciacion_anual"],
                "Depreciación mensual": resultado["depreciacion_mensual"]
            }

            st.session_state.historial_depreciacion.append(registro)

        except ValueError as error:
            st.error(f"Error: {error}")

    st.markdown("---")
    st.subheader("Histórico de resultados")

    if st.session_state.historial_depreciacion:

        df_historial = pd.DataFrame(
            st.session_state.historial_depreciacion
        )

        st.dataframe(
            df_historial.style.format({
                "Costo activo": "S/ {:,.2f}",
                "Valor residual": "S/ {:,.2f}",
                "Depreciación anual": "S/ {:,.2f}",
                "Depreciación mensual": "S/ {:,.2f}"
            }),
            use_container_width=True,
            hide_index=True
        )

        if st.button("🗑️ Limpiar histórico"):
            st.session_state.historial_depreciacion = []
            st.rerun()

    else:
        st.info("Todavía no existen resultados históricos.")


# =========================================================
# EJERCICIO 4 - CLASE EXTERNA + CRUD
# =========================================================

elif opcion == "Ejercicio 4":

    st.title("📦 Ejercicio 4 - Inventario con Clase y CRUD")

    st.markdown(
        """
        En este ejercicio se utiliza la clase `InventarioProducto` de la
        librería externa `librería_clases_proyecto1.py`.

        Se implementan las operaciones CRUD:
        **Crear, Leer, Actualizar y Eliminar**.
        """
    )

    # -----------------------------------------------------
    # CREAR
    # -----------------------------------------------------

    st.subheader("➕ Crear producto")

    col1, col2 = st.columns(2)

    with col1:
        nombre_producto = st.text_input(
            "Nombre del producto",
            key="crear_nombre"
        )

        costo_unitario = st.number_input(
            "Costo unitario",
            min_value=0.0,
            step=0.01,
            format="%.2f",
            key="crear_costo"
        )

        precio_unitario = st.number_input(
            "Precio unitario",
            min_value=0.0,
            step=0.01,
            format="%.2f",
            key="crear_precio"
        )

    with col2:
        stock_actual = st.number_input(
            "Stock actual",
            min_value=0,
            step=1,
            key="crear_stock"
        )

        stock_minimo = st.number_input(
            "Stock mínimo",
            min_value=0,
            step=1,
            key="crear_stock_minimo"
        )

    if st.button("Crear producto", type="primary"):

        if nombre_producto.strip() == "":
            st.warning("Ingrese el nombre del producto.")

        elif costo_unitario <= 0 or precio_unitario <= 0:
            st.warning("Costo y precio deben ser mayores que 0.")

        else:

            try:

                producto_objeto = InventarioProducto(
                    nombre_producto.strip(),
                    costo_unitario,
                    precio_unitario,
                    stock_actual,
                    stock_minimo
                )

                st.session_state.inventario.append(producto_objeto)

                st.success("Producto creado correctamente.")

            except ValueError as error:
                st.error(f"Error: {error}")

    st.markdown("---")

    # -----------------------------------------------------
    # LEER
    # -----------------------------------------------------

    st.subheader("👁️ Leer / visualizar inventario")

    if st.session_state.inventario:

        datos_inventario = []

        for producto in st.session_state.inventario:
            datos_inventario.append(producto.resumen())

        df_inventario = pd.DataFrame(datos_inventario)

        st.dataframe(
            df_inventario.style.format({
                "valor_inventario": "S/ {:,.2f}",
                "margen_unitario": "S/ {:,.2f}",
                "margen_pct": "{:.2f}%"
            }),
            use_container_width=True,
            hide_index=True
        )

    else:
        st.info("No existen productos en el inventario.")

    st.markdown("---")

    # -----------------------------------------------------
    # ACTUALIZAR
    # -----------------------------------------------------

    st.subheader("✏️ Actualizar producto")

    if st.session_state.inventario:

        nombres = [
            producto.nombre
            for producto in st.session_state.inventario
        ]

        producto_seleccionado = st.selectbox(
            "Selecciona el producto a actualizar:",
            nombres,
            key="actualizar_producto"
        )

        indice = nombres.index(producto_seleccionado)
        producto_actual = st.session_state.inventario[indice]

        col1, col2 = st.columns(2)

        with col1:
            nuevo_nombre = st.text_input(
                "Nuevo nombre",
                value=producto_actual.nombre,
                key="nuevo_nombre"
            )

            nuevo_costo = st.number_input(
                "Nuevo costo unitario",
                min_value=0.01,
                value=float(producto_actual.costo_unitario),
                step=0.01,
                key="nuevo_costo"
            )

            nuevo_precio = st.number_input(
                "Nuevo precio unitario",
                min_value=0.01,
                value=float(producto_actual.precio_unitario),
                step=0.01,
                key="nuevo_precio"
            )

        with col2:
            nuevo_stock = st.number_input(
                "Nuevo stock actual",
                min_value=0,
                value=int(producto_actual.stock_actual),
                step=1,
                key="nuevo_stock"
            )

            nuevo_stock_minimo = st.number_input(
                "Nuevo stock mínimo",
                min_value=0,
                value=int(producto_actual.stock_minimo),
                step=1,
                key="nuevo_stock_minimo"
            )

        if st.button("Actualizar producto"):

            if nuevo_nombre.strip() == "":
                st.warning("El nombre no puede estar vacío.")

            else:

                try:

                    producto_actualizado = InventarioProducto(
                        nuevo_nombre.strip(),
                        nuevo_costo,
                        nuevo_precio,
                        nuevo_stock,
                        nuevo_stock_minimo
                    )

                    st.session_state.inventario[indice] = (
                        producto_actualizado
                    )

                    st.success("Producto actualizado correctamente.")
                    st.rerun()

                except ValueError as error:
                    st.error(f"Error: {error}")

    else:
        st.info("No hay productos disponibles para actualizar.")

    st.markdown("---")

    # -----------------------------------------------------
    # ELIMINAR
    # -----------------------------------------------------

    st.subheader("🗑️ Eliminar producto")

    if st.session_state.inventario:

        nombres_eliminar = [
            producto.nombre
            for producto in st.session_state.inventario
        ]

        producto_eliminar = st.selectbox(
            "Selecciona el producto a eliminar:",
            nombres_eliminar,
            key="eliminar_producto"
        )

        if st.button("Eliminar producto"):

            indice_eliminar = nombres_eliminar.index(
                producto_eliminar
            )

            st.session_state.inventario.pop(indice_eliminar)

            st.success("Producto eliminado correctamente.")
            st.rerun()

    else:
        st.info("No hay productos disponibles para eliminar.")
