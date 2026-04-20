import psycopg2
from psycopg2 import Error as PostgresError
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def _get_connection():
    try:
        conexion = psycopg2.connect(DATABASE_URL)
        cursor = conexion.cursor()
        return conexion, cursor
    except PostgresError as e:
        print(f"Error de conexión: {e}")
        return None, None


class ModeloInventario:
    def obtener_productos(self):
        conexion, cursor = _get_connection()
        if not cursor:
            return []
        try:
            cursor.execute("SELECT * FROM productos ORDER BY id")
            result = cursor.fetchall()
            cursor.close()
            conexion.close()
            return result
        except PostgresError as e:
            print(f"Error al obtener productos: {e}")
            return []

    def agregar_producto(self, nombre, cantidad, precio):
        conexion, cursor = _get_connection()
        if not cursor:
            return False
        try:
            cursor.execute(
                "INSERT INTO productos (nombre, cantidad, precio) VALUES (%s, %s, %s)",
                (nombre, cantidad, precio)
            )
            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        except PostgresError as e:
            print(f"Error al agregar producto: {e}")
            conexion.rollback()
            return False

    def actualizar_producto(self, id_producto, cantidad, precio):
        conexion, cursor = _get_connection()
        if not cursor:
            return False
        try:
            cursor.execute(
                "UPDATE productos SET cantidad = %s, precio = %s WHERE id = %s",
                (cantidad, precio, id_producto)
            )
            conexion.commit()
            result = cursor.rowcount > 0
            cursor.close()
            conexion.close()
            return result
        except PostgresError as e:
            print(f"Error al actualizar producto: {e}")
            conexion.rollback()
            return False

    def eliminar_producto(self, id_producto):
        conexion, cursor = _get_connection()
        if not cursor:
            return False
        try:
            cursor.execute("DELETE FROM productos WHERE id = %s", (id_producto,))
            conexion.commit()
            result = cursor.rowcount > 0
            cursor.close()
            conexion.close()
            return result
        except PostgresError as e:
            print(f"Error al eliminar producto: {e}")
            conexion.rollback()
            return False

    def buscar_producto_por_nombre(self, nombre):
        conexion, cursor = _get_connection()
        if not cursor:
            return []
        try:
            cursor.execute(
                "SELECT * FROM productos WHERE nombre LIKE %s ORDER BY id",
                (f"%{nombre}%",)
            )
            result = cursor.fetchall()
            cursor.close()
            conexion.close()
            return result
        except PostgresError as e:
            print(f"Error al buscar producto: {e}")
            return []

    def filtrar_por_precio(self, precio_min, precio_max):
        conexion, cursor = _get_connection()
        if not cursor:
            return []
        try:
            cursor.execute(
                "SELECT * FROM productos WHERE precio BETWEEN %s AND %s ORDER BY id",
                (precio_min, precio_max)
            )
            result = cursor.fetchall()
            cursor.close()
            conexion.close()
            return result
        except PostgresError as e:
            print(f"Error al filtrar productos: {e}")
            return []

    def calcular_valor_total(self):
        conexion, cursor = _get_connection()
        if not cursor:
            return 0.0
        try:
            cursor.execute("SELECT cantidad, precio FROM productos")
            productos = cursor.fetchall()
            total = sum(cantidad * precio for cantidad, precio in productos)
            cursor.close()
            conexion.close()
            return total
        except PostgresError as e:
            print(f"Error al calcular valor total: {e}")
            return 0.0
