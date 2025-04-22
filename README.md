# Control_inventario_mvc

# **¿Qué puedes hacer?**

- **Ver todos los productos** que están en el inventario.  
- **Agregar nuevos productos** al inventario.  
- **Actualizar productos existentes** cambiando cantidad o precio.  
- **Eliminar productos** del inventario.  
- **Buscar un producto** por su nombre.  
- **Filtrar productos** por un rango de precios.  
- **Calcular el valor total** del inventario.

---

# **¿Cómo está estructurado?**

**Arquitectura**  
- **Modelo (modelo.py):** Se encarga de toda la conexión y operaciones en la base de datos MySQL.  
- **Vista (vista.py):** Se encarga de mostrar información y pedir datos al usuario.  
- **Controlador (controlador.py):** Conecta el modelo y la vista, controla el flujo del programa.  
- **main.py:** Es el archivo principal que inicia la aplicación.

---

# **¿Cómo se organizan los archivos?**

## **1. modelo.py**
```python
def obtener_productos(self):
def agregar_producto(self, nombre, cantidad, precio):
def actualizar_producto(self, id_producto, cantidad, precio):
def eliminar_producto(self, id_producto):
def buscar_producto_por_nombre(self, nombre):
def filtrar_por_precio(self, precio_min, precio_max):
def calcular_valor_total(self):
```

## **2. vista.py**
```python
def mostrar_menu():
def mostrar_productos(productos):
def solicitar_datos_producto():
def solicitar_id_producto():
def solicitar_datos_actualizacion():
def solicitar_nombre_producto():
def solicitar_rango_precios():
def mostrar_valor_total(valor):
```

## **3. controlador.py**
```python
def iniciar():
```

## **4. main.py**
```python
from controlador import ControladorInventario
```

---

# **Notas**

- Todas las consultas SQL son parametrizadas para evitar inyección SQL.  
- Se recomienda cerrar siempre las conexiones a la base de datos para evitar problemas de recursos.  
- El proyecto está estructurado siguiendo el patrón MVC para una mejor organización y mantenimiento del código.
