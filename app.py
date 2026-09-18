import streamlit as st
import numpy as np
import pandas as pd

from libreria_funciones_proyecto1 import calcular_depreciacion_linea_recta
from libreria_clases_proyecto1 import InventarioProducto


st.set_page_config(
    page_title="Proyecto Python Fundamentals",
    page_icon="🐍",
    layout="wide"
)


# ============================================================
# CONFIGURACIÓN INICIAL
# ============================================================

if "movimientos" not in st.session_state:
    st.session_state.movimientos = []

if "productos_np" not in st.session_state:
    st.session_state.productos_np = {
        "nombre": np.array([], dtype=str),
        "categoria": np.array([], dtype=str),
        "precio": np.array([], dtype=float),
        "cantidad": np.array([], dtype=int),
        "total": np.array([], dtype=float)
    }

if "historial_depreciacion" not in st.session_state:
    st.session_state.historial_depreciacion = []

if "inventario" not in st.session_state:
    st.session_state.inventario = []


# ============================================================
# MENÚ LATERAL
# ============================================================

st.sidebar.title("📚 Menú")

pagina = st.sidebar.selectbox(
    "Selecciona una sección:",
    [
        "Home",
        "Ejercicio 1",
        "Ejercicio 2",
        "Ejercicio 3",
        "Ejercicio 4"
    ]
)


# ============================================================
# HOME
# ============================================================

if pagina == "Home":

    st.title("🐍 Proyecto Aplicado en Streamlit")

    st.subheader(
        "Especialización en Python for Analytics - Módulo 1"
    )

    st.markdown("## Información del estudiante")

    st.write("**Nombre:** Sebastián Ccala")
    st.write("**Módulo:** Python Fundamentals")
    st.write("**Año:** 2026")

    st.markdown("## Descripción del proyecto")

    st.write(
        """
        Esta aplicación ha sido desarrollada utilizando Python y Streamlit
        con el objetivo de aplicar los conocimientos aprendidos durante
        el módulo Python Fundamentals.

        El proyecto integra listas, arreglos de NumPy, DataFrames,
        funciones externas y programación orientada a objetos mediante
        operaciones CRUD.
        """
    )

    st.markdown("## Tecnologías utilizadas")

    st.write("- Python")
    st.write("- Streamlit")
    st.write("- NumPy")
    st.write("- Pandas")
    st.write("- Programación Orientada a Objetos")


# ============================================================
# EJERCICIO 1
# ============================================================

elif pagina == "Ejercicio 1":

    st.title("💰 Ejercicio 1 - Flujo de caja con listas")

    st.markdown(
        """
        En este ejercicio se registran movimientos financieros
        utilizando una lista de Python.

        Cada movimiento contiene:
        - Concepto
        - Tipo de movimiento
        - Valor
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        concepto = st.text_input(
            "Concepto",
            placeholder="Ej. Venta de servicio"
        )

    with col2:

        tipo = st.selectbox(
            "Tipo de movimiento",
            ["Ingreso", "Gasto"]
        )

    with col3:

        valor = st.number_input(
            "Valor (S/)",
            min_value=0.0,
            step=10.0,
            format="%.2f"
        )

    if st.button("➕ Agregar movimiento"):

        if concepto.strip() == "":

            st.warning("Ingresa un concepto.")

        elif valor <= 0:

            st.warning("El valor debe ser mayor que cero.")

        else:

            movimiento = {
                "concepto": concepto,
                "tipo": tipo,
                "valor": valor
            }

            st.session_state.movimientos.append(movimiento)

            st.success("Movimiento agregado correctamente.")

    st.markdown("### Movimientos registrados")

    if len(st.session_state.movimientos) > 0:

        df_movimientos = pd.DataFrame(
            st.session_state.movimientos
        )

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
            "Saldo final",
            f"S/ {saldo:,.2f}"
        )

        if saldo >= 0:

            st.success(
                "El flujo de caja está a favor."
            )

        else:

            st.error(
                "El flujo de caja está en contra."
            )

        if st.button("🗑️ Limpiar movimientos"):

            st.session_state.movimientos = []

            st.rerun()

    else:

        st.info(
            "Todavía no hay movimientos registrados."
        )


# ============================================================
# EJERCICIO 2
# ============================================================

elif pagina == "Ejercicio 2":

    st.title(
        "📦 Ejercicio 2 - Registro con NumPy y DataFrame"
    )

    st.markdown(
        """
        En este ejercicio se registran productos utilizando
        arreglos de NumPy.

        Posteriormente los arreglos son convertidos en un
        DataFrame de Pandas.
        """
    )

    col1, col2 = st.columns(2)

    with col1:

        nombre = st.text_input(
            "Nombre del producto"
        )

        categoria = st.selectbox(
            "Categoría",
            [
                "Activo",
                "Suministro",
                "Servicio",
                "Mercadería",
                "Otro"
            ]
        )

    with col2:

        precio = st.number_input(
            "Precio unitario (S/)",
            min_value=0.0,
            step=10.0,
            format="%.2f"
        )

        cantidad = st.number_input(
            "Cantidad",
            min_value=1,
            step=1
        )

    if st.button("➕ Agregar producto"):

        if nombre.strip() == "":

            st.warning(
                "Ingresa el nombre del producto."
            )

        elif precio <= 0:

            st.warning(
                "El precio debe ser mayor que cero."
            )

        else:

            total = precio * cantidad

            st.session_state.productos_np["nombre"] = np.append(
                st.session_state.productos_np["nombre"],
                nombre
            )

            st.session_state.productos_np["categoria"] = np.append(
                st.session_state.productos_np["categoria"],
                categoria
            )

            st.session_state.productos_np["precio"] = np.append(
                st.session_state.productos_np["precio"],
                precio
            )

            st.session_state.productos_np["cantidad"] = np.append(
                st.session_state.productos_np["cantidad"],
                cantidad
            )

            st.session_state.productos_np["total"] = np.append(
                st.session_state.productos_np["total"],
                total
            )

            st.success(
                "Producto agregado correctamente."
            )

    st.markdown("### Tabla de productos")

    arrays = st.session_state.productos_np

    if len(arrays["nombre"]) > 0:

        df_productos = pd.DataFrame(arrays)

        df_productos.columns = [
            "Producto",
            "Categoría",
            "Precio",
            "Cantidad",
            "Total"
        ]

        st.dataframe(
            df_productos,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "Todavía no hay productos registrados."
        )


# ============================================================
# EJERCICIO 3
# ============================================================

elif pagina == "Ejercicio 3":

    st.title(
        "🧾 Ejercicio 3 - Función desde librería externa"
    )

    st.markdown(
        """
        En este ejercicio utilizaremos una función de la
        librería externa:

        `libreria_funciones_proyecto1.py`

        La función seleccionada está relacionada con el
        área contable y permite calcular la depreciación
        de un activo mediante el método de línea recta.
        """
    )

    funcion = st.selectbox(
        "Selecciona la función",
        [
            "calcular_depreciacion_linea_recta"
        ]
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        costo_activo = st.number_input(
            "Costo del activo (S/)",
            min_value=0.01,
            value=12000.0,
            step=500.0,
            format="%.2f"
        )

    with col2:

        valor_residual = st.number_input(
            "Valor residual (S/)",
            min_value=0.0,
            value=1000.0,
            step=100.0,
            format="%.2f"
        )

    with col3:

        vida_util = st.number_input(
            "Vida útil (años)",
            min_value=1,
            value=5,
            step=1
        )

    if st.button("▶️ Ejecutar función"):

        try:

            resultado = calcular_depreciacion_linea_recta(
                costo_activo,
                valor_residual,
                vida_util
            )

            st.success(
                "Función ejecutada correctamente."
            )

            col1, col2 = st.columns(2)

            col1.metric(
                "Depreciación anual",
                f"S/ {resultado['depreciacion_anual']:,.2f}"
            )

            col2.metric(
                "Depreciación mensual",
                f"S/ {resultado['depreciacion_mensual']:,.2f}"
            )

            registro = {

                "Costo activo": costo_activo,

                "Valor residual": valor_residual,

                "Vida útil": vida_util,

                "Depreciación anual":
                    resultado["depreciacion_anual"],

                "Depreciación mensual":
                    resultado["depreciacion_mensual"]
            }

            st.session_state.historial_depreciacion.append(
                registro
            )

        except ValueError as error:

            st.error(
                f"Error: {error}"
            )

    st.markdown(
        "### Histórico de resultados"
    )

    if len(st.session_state.historial_depreciacion) > 0:

        df_historial = pd.DataFrame(
            st.session_state.historial_depreciacion
        )

        st.dataframe(
            df_historial,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "Todavía no se ha ejecutado la función."
        )


# ============================================================
# EJERCICIO 4
# ============================================================

elif pagina == "Ejercicio 4":

    st.title(
        "🏷️ Ejercicio 4 - Clase externa y CRUD"
    )

    st.markdown(
        """
        En este ejercicio se utiliza la clase:

        `InventarioProducto`

        perteneciente a la librería externa
        `libreria_clases_proyecto1.py`.

        Se implementan las operaciones CRUD:

        - Crear
        - Leer
        - Actualizar
        - Eliminar
        """
    )

    accion = st.radio(
        "Selecciona una operación:",
        [
            "Crear",
            "Leer",
            "Actualizar",
            "Eliminar"
        ],
        horizontal=True
    )


    # ========================================================
    # CREAR
    # ========================================================

    if accion == "Crear":

        st.subheader(
            "Crear producto"
        )

        col1, col2 = st.columns(2)

        with col1:

            nombre = st.text_input(
                "Nombre del producto",
                key="crear_nombre"
            )

            costo = st.number_input(
                "Costo unitario (S/)",
                min_value=0.01,
                step=10.0,
                format="%.2f",
                key="crear_costo"
            )

            precio = st.number_input(
                "Precio unitario (S/)",
                min_value=0.01,
                step=10.0,
                format="%.2f",
                key="crear_precio"
            )

        with col2:

            stock = st.number_input(
                "Stock actual",
                min_value=0,
                step=1,
                key="crear_stock"
            )

            stock_minimo = st.number_input(
                "Stock mínimo",
                min_value=0,
                step=1,
                key="crear_minimo"
            )

        if st.button("➕ Crear producto"):

            try:

                producto = InventarioProducto(
                    nombre,
                    costo,
                    precio,
                    stock,
                    stock_minimo
                )

                st.session_state.inventario.append(
                    producto
                )

                st.success(
                    "Producto creado correctamente."
                )

            except ValueError as error:

                st.error(
                    f"Error: {error}"
                )


    # ========================================================
    # LEER
    # ========================================================

    elif accion == "Leer":

        st.subheader(
            "Productos registrados"
        )

        if len(st.session_state.inventario) > 0:

            registros = []

            for producto in st.session_state.inventario:

                registros.append(
                    producto.resumen()
                )

            df_inventario = pd.DataFrame(
                registros
            )

            st.dataframe(
                df_inventario,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No hay productos registrados."
            )


    # ========================================================
    # ACTUALIZAR
    # ========================================================

    elif accion == "Actualizar":

        st.subheader(
            "Actualizar producto"
        )

        if len(st.session_state.inventario) == 0:

            st.info(
                "No hay productos para actualizar."
            )

        else:

            nombres = [
                producto.nombre
                for producto in st.session_state.inventario
            ]

            seleccionado = st.selectbox(
                "Selecciona el producto",
                nombres
            )

            indice = nombres.index(
                seleccionado
            )

            producto = st.session_state.inventario[
                indice
            ]

            nuevo_nombre = st.text_input(
                "Nombre",
                value=producto.nombre
            )

            nuevo_costo = st.number_input(
                "Costo unitario",
                min_value=0.01,
                value=float(
                    producto.costo_unitario
                )
            )

            nuevo_precio = st.number_input(
                "Precio unitario",
                min_value=0.01,
                value=float(
                    producto.precio_unitario
                )
            )

            nuevo_stock = st.number_input(
                "Stock actual",
                min_value=0,
                value=int(
                    producto.stock_actual
                )
            )

            nuevo_minimo = st.number_input(
                "Stock mínimo",
                min_value=0,
                value=int(
                    producto.stock_minimo
                )
            )

            if st.button(
                "✏️ Guardar cambios"
            ):

                producto.nombre = nuevo_nombre

                producto.costo_unitario = nuevo_costo

                producto.precio_unitario = nuevo_precio

                producto.stock_actual = nuevo_stock

                producto.stock_minimo = nuevo_minimo

                st.success(
                    "Producto actualizado correctamente."
                )


    # ========================================================
    # ELIMINAR
    # ========================================================

    elif accion == "Eliminar":

        st.subheader(
            "Eliminar producto"
        )

        if len(st.session_state.inventario) == 0:

            st.info(
                "No hay productos para eliminar."
            )

        else:

            nombres = [
                producto.nombre
                for producto in st.session_state.inventario
            ]

            seleccionado = st.selectbox(
                "Selecciona el producto",
                nombres
            )

            if st.button(
                "🗑️ Eliminar producto"
            ):

                indice = nombres.index(
                    seleccionado
                )

                st.session_state.inventario.pop(
                    indice
                )

                st.success(
                    "Producto eliminado correctamente."
                )
                def calcular_depreciacion_linea_recta(
    costo_activo: float,
    valor_residual: float,
    vida_util_anios: int
) -> dict:

    validar_positivo(
        costo_activo,
        "costo_activo"
    )

    validar_positivo(
        valor_residual,
        "valor_residual",
        permitir_cero=True
    )

    validar_positivo(
        vida_util_anios,
        "vida_util_anios"
    )

    if valor_residual >= costo_activo:

        raise ValueError(
            "valor_residual debe ser menor que costo_activo."
        )

    depreciacion_anual = (
        costo_activo - valor_residual
    ) / vida_util_anios

    depreciacion_mensual = (
        depreciacion_anual / 12
    )

    return {

        "depreciacion_anual":
            round(depreciacion_anual, 2),

        "depreciacion_mensual":
            round(depreciacion_mensual, 2)
    }
