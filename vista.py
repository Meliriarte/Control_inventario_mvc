class VistaInventario:
    @staticmethod
    def mostrar_menu():
        print("\n--- Menú del Inventario ---")
        print("1. Ver productos")
        print("2. Agregar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto por nombre")
        print("6. Filtrar productos por precio")
        print("7. Calcular valor total del inventario")
        print("8. Salir")
        return input("Seleccione una opción: ")

    @staticmethod
    def mostrar_productos(productos):
        print("\n--- Productos en inventario ---")
        if productos:
            for producto in productos:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[2]}, Precio: ${producto[3]}")
        else:
            print("No se encontraron productos.")
        print("---")

    @staticmethod
    def solicitar_datos_producto():
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = VistaInventario._leer_numero_entero("Ingrese la cantidad del producto: ")
        precio = VistaInventario._leer_numero_flotante("Ingrese el precio del producto: ")
        return nombre, cantidad, precio

    @staticmethod
    def solicitar_id_producto():
        return VistaInventario._leer_numero_entero("Ingrese el ID del producto: ")

    @staticmethod
    def solicitar_datos_actualizacion():
        cantidad = VistaInventario._leer_numero_entero("Ingrese la nueva cantidad: ")
        precio = VistaInventario._leer_numero_flotante("Ingrese el nuevo precio: ")
        return cantidad, precio

    @staticmethod
    def solicitar_nombre_producto():
        return input("Ingrese el nombre del producto a buscar: ")

    @staticmethod
    def solicitar_rango_precios():
        precio_min = VistaInventario._leer_numero_flotante("Ingrese el precio mínimo: ")
        precio_max = VistaInventario._leer_numero_flotante("Ingrese el precio máximo: ")
        return precio_min, precio_max

    @staticmethod
    def mostrar_valor_total(valor):
        print(f"\nEl valor total del inventario es: ${valor:.2f}")

    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)

    @staticmethod
    def _leer_numero_entero(mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")

    @staticmethod
    def _leer_numero_flotante(mensaje):
        while True:
            try:
                return float(input(mensaje))
            except ValueError:
                print("Error: Debe ingresar un número válido.")

    @staticmethod
    def confirmar_accion(mensaje):
        respuesta = input(f"{mensaje} (s/n): ").lower().strip()
        return respuesta == 's'
