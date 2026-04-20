from modelo import ModeloInventario
from vista import VistaInventario

class ControladorInventario:
    def __init__(self):
        self.modelo = ModeloInventario()
        self.vista = VistaInventario()

    def iniciar(self):
        if not self.modelo._esta_conectado():
            self.vista.mostrar_mensaje("No se pudo conectar a la base de datos. Saliendo...")
            return

        opcion = ""
        while opcion != "8":
            opcion = self.vista.mostrar_menu()

            try:
                if opcion == "1":
                    productos = self.modelo.obtener_productos()
                    self.vista.mostrar_productos(productos)

                elif opcion == "2":
                    nombre, cantidad, precio = self.vista.solicitar_datos_producto()
                    if self.modelo.agregar_producto(nombre, cantidad, precio):
                        self.vista.mostrar_mensaje("Producto agregado exitosamente.")
                    else:
                        self.vista.mostrar_mensaje("Error al agregar producto.")

                elif opcion == "3":
                    id_producto = self.vista.solicitar_id_producto()
                    cantidad, precio = self.vista.solicitar_datos_actualizacion()
                    if self.modelo.actualizar_producto(id_producto, cantidad, precio):
                        self.vista.mostrar_mensaje("Producto actualizado exitosamente.")
                    else:
                        self.vista.mostrar_mensaje("Error: El producto no existe o no se pudo actualizar.")

                elif opcion == "4":
                    id_producto = self.vista.solicitar_id_producto()
                    if self.vista.confirmar_accion(f"¿Está seguro de eliminar el producto con ID {id_producto}?"):
                        if self.modelo.eliminar_producto(id_producto):
                            self.vista.mostrar_mensaje("Producto eliminado exitosamente.")
                        else:
                            self.vista.mostrar_mensaje("Error: El producto no existe o no se pudo eliminar.")
                    else:
                        self.vista.mostrar_mensaje("Eliminación cancelada.")

                elif opcion == "5":
                    nombre = self.vista.solicitar_nombre_producto()
                    resultados = self.modelo.buscar_producto_por_nombre(nombre)
                    self.vista.mostrar_productos(resultados)

                elif opcion == "6":
                    precio_min, precio_max = self.vista.solicitar_rango_precios()
                    resultados = self.modelo.filtrar_por_precio(precio_min, precio_max)
                    self.vista.mostrar_productos(resultados)

                elif opcion == "7":
                    total = self.modelo.calcular_valor_total()
                    self.vista.mostrar_valor_total(total)

                elif opcion == "8":
                    self.vista.mostrar_mensaje("Saliendo...")

                else:
                    self.vista.mostrar_mensaje("Opción inválida. Intente de nuevo.")

            except Exception as e:
                self.vista.mostrar_mensaje(f"Error inesperado: {e}")

        self.modelo.cerrar_conexion()
