import streamlit as st
import numpy as np
import pandas as pd

from libreria_funciones_proyecto1 import calcular_depreciacion_linea_recta
from libreria_clases_proyecto1 import InventarioProducto

st.set_page_config(
    page_title="Proyecto Python Fundamentals",
    layout="wide")


if "movimientos" not in st.session_state:
    st.session_state.movimientos = []

if "productos_np" not in st.session_state:
    st.session_state.productos_np = {
        "nombre": np.array([], dtype=str),
        "categoria": np.array([], dtype=str),
        "precio": np.array([], dtype=float),
        "cantidad": np.array([], dtype=int),
        "total": np.array([], dtype=float),
    }

if "historial_depreciacion" not in st.session_state:
    st.session_state.historial_depreciacion = []

if "inventario" not in st.session_state:
    st.session_state.inventario = []


# ============================================================
# MENÚ LATERAL
# ============================================================

st.sidebar.image("LOGO.png")

st.sidebar.title("## 📚 Menú")
pagina = st.sidebar.selectbox(
    "Selecciona una sección:",
    [
        "Home",
        "Ejercicio 1",
        "Ejercicio 2",
        "Ejercicio 3",
        "Ejercicio 4",
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("Proyecto aplicado – Python Fundamentals")


# ============================================================
# HOME
# ============================================================

if pagina == "Home":
    st.title("PRIMER PROYECTO PYTHON - MÓDULO 1")
    
    st.write("**Creado por:** Sebastián Ccala")
    
    st.write("**Año:** 2026")
    
    st.image("LOGO 2.png",width =600)
    
    st.markdown("## Descripción del proyecto")
    st.write(
        "Aplicación interactiva desarrollada en Streamlit para demostrar "
        "el uso de listas, arreglos de NumPy y DataFrames")

    st.markdown("## Tecnologías utilizadas")
    st.write("- Python")
    st.write("- Streamlit")
    st.write("- NumPy")
    st.write("- Pandas")
    st.write("- Programación orientada a objetos (POO)")

    st.info(
        "La aplicación está organizada en cuatro ejercicios y cada sección "
        "puede utilizarse de forma independiente desde el menú lateral."
    )


# ============================================================
# EJERCICIO 1 – FLUJO DE CAJA CON LISTAS
# ============================================================

elif pagina == "Ejercicio 1":
    st.title("💰 Ejercicio 1 – Flujo de caja con listas")

    st.markdown(
        """
        Registra movimientos financieros utilizando una **lista de Python**.
        Cada movimiento contiene concepto, tipo y valor.
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        concepto = st.text_input("Concepto", placeholder="Ej. Venta de servicio")

    with col2:
        tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])

    with col3:
        valor = st.number_input(
            "Valor (S/)",
            min_value=0.0,
            step=10.0,
            format="%.2f"
        )

    if st.button("➕ Agregar movimiento", type="primary"):
        if concepto.strip() == "":
            st.warning("Ingresa un concepto.")
        elif valor <= 0:
            st.warning("El valor debe ser mayor que cero.")
        else:
            st.session_state.movimientos.append(
                {
                    "concepto": concepto.strip(),
                    "tipo": tipo,
                    "valor": valor,
                }
            )
            st.success("Movimiento agregado correctamente.")

    st.markdown("### Movimientos registrados")

    if st.session_state.movimientos:
        df_movimientos = pd.DataFrame(st.session_state.movimientos)
        st.dataframe(df_movimientos, use_container_width=True, hide_index=True)

        total_ingresos = sum(
            m["valor"] for m in st.session_state.movimientos
            if m["tipo"] == "Ingreso"
        )
        total_gastos = sum(
            m["valor"] for m in st.session_state.movimientos
            if m["tipo"] == "Gasto"
        )
        saldo = total_ingresos - total_gastos

        c1, c2, c3 = st.columns(3)
        c1.metric("Total ingresos", f"S/ {total_ingresos:,.2f}")
        c2.metric("Total gastos", f"S/ {total_gastos:,.2f}")
        c3.metric("Saldo final", f"S/ {saldo:,.2f}")

        if saldo >= 0:
            st.success("El flujo de caja está a favor.")
        else:
            st.error("El flujo de caja está en contra.")

        if st.button("🗑️ Limpiar movimientos"):
            st.session_state.movimientos = []
            st.rerun()
    else:
        st.info("Todavía no hay movimientos registrados.")


# ============================================================
# EJERCICIO 2 – NUMPY + DATAFRAME
# ============================================================

elif pagina == "Ejercicio 2":
    st.title("📦 Ejercicio 2 – Registro con NumPy y DataFrame")

    st.markdown(
        """
        Registra productos mediante widgets. Los datos se almacenan primero
        en **arreglos de NumPy** y luego se convierten en un **DataFrame de Pandas**.
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        nombre = st.text_input("Nombre del producto", placeholder="Ej. Laptop")
        categoria = st.selectbox(
            "Categoría",
            ["Activo", "Suministro", "Servicio", "Mercadería", "Otro"]
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

    if st.button("➕ Agregar producto", type="primary"):
        if nombre.strip() == "":
            st.warning("Ingresa el nombre del producto.")
        elif precio <= 0:
            st.warning("El precio debe ser mayor que cero.")
        else:
            total = precio * cantidad

            st.session_state.productos_np["nombre"] = np.append(
                st.session_state.productos_np["nombre"], nombre.strip()
            )
            st.session_state.productos_np["categoria"] = np.append(
                st.session_state.productos_np["categoria"], categoria
            )
            st.session_state.productos_np["precio"] = np.append(
                st.session_state.productos_np["precio"], precio
            )
            st.session_state.productos_np["cantidad"] = np.append(
                st.session_state.productos_np["cantidad"], cantidad
            )
            st.session_state.productos_np["total"] = np.append(
                st.session_state.productos_np["total"], total
            )

            st.success("Producto agregado correctamente.")

    st.markdown("### Tabla actualizada")

    arrays = st.session_state.productos_np
    if len(arrays["nombre"]) > 0:
        df_productos = pd.DataFrame(arrays)
        df_productos.columns = [
            "Producto", "Categoría", "Precio", "Cantidad", "Total"
        ]

        df_productos["Precio"] = df_productos["Precio"].round(2)
        df_productos["Total"] = df_productos["Total"].round(2)

        st.dataframe(
            df_productos,
            use_container_width=True,
            hide_index=True
        )

        if st.button("🗑️ Limpiar productos"):
            for clave, dtype in [
                ("nombre", str),
                ("categoria", str),
                ("precio", float),
                ("cantidad", int),
                ("total", float),
            ]:
                st.session_state.productos_np[clave] = np.array([], dtype=dtype)
            st.rerun()
    else:
        st.info("Todavía no hay productos registrados.")


# ============================================================
# EJERCICIO 3 – FUNCIÓN EXTERNA
# ============================================================

elif pagina == "Ejercicio 3":
    st.title("🧾 Ejercicio 3 – Función desde librería externa")

    st.markdown(
        """
        Se utiliza la función **calcular_depreciacion_linea_recta()**
        de la librería externa `libreria_funciones_proyecto1.py`.

        La función está relacionada con el área contable porque permite
        calcular la depreciación anual y mensual de un activo.
        """
    )

    st.info(
        "Fórmula: depreciación anual = "
        "(costo del activo − valor residual) / vida útil"
    )

    funcion = st.selectbox(
        "Selecciona la función",
        ["calcular_depreciacion_linea_recta"]
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

    if st.button("▶️ Ejecutar función", type="primary"):
        try:
            resultado = calcular_depreciacion_linea_recta(
                costo_activo,
                valor_residual,
                vida_util
            )

            st.success("Función ejecutada correctamente.")

            r1, r2 = st.columns(2)
            r1.metric(
                "Depreciación anual",
                f"S/ {resultado['depreciacion_anual']:,.2f}"
            )
            r2.metric(
                "Depreciación mensual",
                f"S/ {resultado['depreciacion_mensual']:,.2f}"
            )

            registro = {
                "Costo activo": costo_activo,
                "Valor residual": valor_residual,
                "Vida útil (años)": vida_util,
                "Depreciación anual": resultado["depreciacion_anual"],
                "Depreciación mensual": resultado["depreciacion_mensual"],
            }

            st.session_state.historial_depreciacion.append(registro)

        except ValueError as error:
            st.error(f"Error de validación: {error}")

    st.markdown("### Histórico de resultados")

    if st.session_state.historial_depreciacion:
        df_historial = pd.DataFrame(st.session_state.historial_depreciacion)
        st.dataframe(
            df_historial,
            use_container_width=True,
            hide_index=True
        )

        if st.button("🗑️ Limpiar histórico"):
            st.session_state.historial_depreciacion = []
            st.rerun()
    else:
        st.info("Todavía no se ha ejecutado la función.")


# ============================================================
# EJERCICIO 4 – CLASE EXTERNA + CRUD
# ============================================================

elif pagina == "Ejercicio 4":
    st.title("🏷️ Ejercicio 4 – Clase externa con CRUD")

    st.markdown(
        """
        Se utiliza la clase **InventarioProducto** de la librería externa
        `libreria_clases_proyecto1.py`.

        Se implementan las operaciones CRUD:
        **Crear, Leer, Actualizar y Eliminar**.
        """
    )

    accion = st.radio(
        "Selecciona una operación:",
        ["Crear", "Leer", "Actualizar", "Eliminar"],
        horizontal=True
    )

    # ---------------- CREATE ----------------
    if accion == "Crear":
        st.markdown("### Crear producto")

        col1, col2 = st.columns(2)

        with col1:
            nombre_nuevo = st.text_input(
                "Nombre del producto",
                key="crear_nombre"
            )
            costo_nuevo = st.number_input(
                "Costo unitario (S/)",
                min_value=0.01,
                step=10.0,
                format="%.2f",
                key="crear_costo"
            )
            precio_nuevo = st.number_input(
                "Precio unitario (S/)",
                min_value=0.01,
                step=10.0,
                format="%.2f",
                key="crear_precio"
            )

        with col2:
            stock_nuevo = st.number_input(
                "Stock actual",
                min_value=0,
                step=1,
                key="crear_stock"
            )
            minimo_nuevo = st.number_input(
                "Stock mínimo",
                min_value=0,
                step=1,
                key="crear_minimo"
            )

        if st.button("➕ Crear producto", type="primary"):
            if nombre_nuevo.strip() == "":
                st.warning("Ingresa el nombre del producto.")
            else:
                try:
                    producto = InventarioProducto(
                        nombre_nuevo.strip(),
                        costo_nuevo,
                        precio_nuevo,
                        stock_nuevo,
                        minimo_nuevo
                    )

                    st.session_state.inventario.append(producto)
                    st.success("Producto creado correctamente.")
                    st.rerun()

                except ValueError as error:
                    st.error(f"Error de validación: {error}")

    # ---------------- READ ----------------
    elif accion == "Leer":
        st.markdown("### Productos registrados")

        if st.session_state.inventario:
            registros = [
                producto.resumen()
                for producto in st.session_state.inventario
            ]

            df_inventario = pd.DataFrame(registros)
            st.dataframe(
                df_inventario,
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info("No hay productos registrados.")

    # ---------------- UPDATE ----------------
    elif accion == "Actualizar":
        st.markdown("### Actualizar producto")

        if not st.session_state.inventario:
            st.info("No hay productos para actualizar.")
        else:
            nombres = [
                producto.nombre
                for producto in st.session_state.inventario
            ]

            seleccionado = st.selectbox(
                "Selecciona el producto",
                nombres,
                key="actualizar_producto"
            )

            indice = nombres.index(seleccionado)
            producto_actual = st.session_state.inventario[indice]

            col1, col2 = st.columns(2)

            with col1:
                nuevo_nombre = st.text_input(
                    "Nombre",
                    value=producto_actual.nombre,
                    key="update_nombre"
                )
                nuevo_costo = st.number_input(
                    "Costo unitario (S/)",
                    min_value=0.01,
                    value=float(producto_actual.costo_unitario),
                    step=10.0,
                    format="%.2f",
                    key="update_costo"
                )
                nuevo_precio = st.number_input(
                    "Precio unitario (S/)",
                    min_value=0.01,
                    value=float(producto_actual.precio_unitario),
                    step=10.0,
                    format="%.2f",
                    key="update_precio"
                )

            with col2:
                nuevo_stock = st.number_input(
                    "Stock actual",
                    min_value=0,
                    value=int(producto_actual.stock_actual),
                    step=1,
                    key="update_stock"
                )
                nuevo_minimo = st.number_input(
                    "Stock mínimo",
                    min_value=0,
                    value=int(producto_actual.stock_minimo),
                    step=1,
                    key="update_minimo"
                )

            if st.button("✏️ Guardar cambios", type="primary"):
                if nuevo_nombre.strip() == "":
                    st.warning("El nombre no puede estar vacío.")
                else:
                    try:
                        producto_actual.nombre = nuevo_nombre.strip()
                        producto_actual.costo_unitario = nuevo_costo
                        producto_actual.precio_unitario = nuevo_precio
                        producto_actual.stock_actual = nuevo_stock
                        producto_actual.stock_minimo = nuevo_minimo

                        # Validamos el nuevo estado con la misma lógica
                        # de la clase externa.
                        InventarioProducto(
                            producto_actual.nombre,
                            producto_actual.costo_unitario,
                            producto_actual.precio_unitario,
                            producto_actual.stock_actual,
                            producto_actual.stock_minimo
                        )

                        st.success("Producto actualizado correctamente.")
                        st.rerun()

                    except ValueError as error:
                        st.error(f"Error de validación: {error}")

    # ---------------- DELETE ----------------
    elif accion == "Eliminar":
        st.markdown("### Eliminar producto")

        if not st.session_state.inventario:
            st.info("No hay productos para eliminar.")
        else:
            nombres = [
                producto.nombre
                for producto in st.session_state.inventario
            ]

            seleccionado = st.selectbox(
                "Selecciona el producto",
                nombres,
                key="eliminar_producto"
            )

            if st.button("🗑️ Eliminar producto", type="primary"):
                indice = nombres.index(seleccionado)
                st.session_state.inventario.pop(indice)
                st.success("Producto eliminado correctamente.")
                st.rerun()
