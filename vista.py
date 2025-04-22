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
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        return nombre, cantidad, precio

    @staticmethod
    def solicitar_id_producto():
        return int(input("Ingrese el ID del producto: "))

    @staticmethod
    def solicitar_datos_actualizacion():
        cantidad = int(input("Ingrese la nueva cantidad: "))
        precio = float(input("Ingrese el nuevo precio: "))
        return cantidad, precio

    @staticmethod
    def solicitar_nombre_producto():
        return input("Ingrese el nombre del producto a buscar: ")

    @staticmethod
    def solicitar_rango_precios():
        precio_min = float(input("Ingrese el precio mínimo: "))
        precio_max = float(input("Ingrese el precio máximo: "))
        return precio_min, precio_max

    @staticmethod
    def mostrar_valor_total(valor):
        print(f"\nEl valor total del inventario es: ${valor:.2f}")

    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)