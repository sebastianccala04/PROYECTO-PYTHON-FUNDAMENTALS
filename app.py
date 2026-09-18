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
            st.session_state.cantidades)

        # Crear DataFrame
        df_productos = pd.DataFrame({
            "Producto": st.session_state.productos,
            "Categoría": st.session_state.categorias,
            "Precio": st.session_state.precios,
            "Cantidad": st.session_state.cantidades,
            "Total": totales})

        st.subheader("Productos registrados")

        st.dataframe(
            df_productos,
            use_container_width=True)

    else:

        st.info("Todavía no hay productos registrados.")
