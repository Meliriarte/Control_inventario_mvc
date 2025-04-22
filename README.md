# Control_inventario_mvc

# **¿Qué problemas resuelve?**

- Permite llevar un control ordenado de los productos sin necesidad de hojas de Excel.  
- Facilita agregar, consultar, actualizar y eliminar productos de manera rápida.  
- Ayuda a realizar búsquedas de productos específicas por nombre o por rango de precios.  
- Calcula el valor total del inventario de manera automática para control financiero.

---

# **¿Qué puedes hacer con esta aplicación?**

- **Ver todos los productos** que están en el inventario.  
- **Agregar nuevos productos** al inventario.  
- **Actualizar productos existentes** cambiando cantidad o precio.  
- **Eliminar productos** del inventario.  
- **Buscar un producto** por su nombre.  
- **Filtrar productos** por un rango de precios.  
- **Calcular el valor total** del inventario.

---

# **¿Cómo está estructurado el proyecto?**

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

# **Pasos para ejecutar el proyecto**

1. Instalar la librería `pyodbc`:
```bash
pip install pyodbc
```

2. Configurar la base de datos en MySQL:
```sql
CREATE DATABASE control_inventario;

USE control_inventario;

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    cantidad INT NOT NULL,
    precio FLOAT NOT NULL
);
```

3. Verificar que en `modelo.py` esté la configuración correcta de conexión:
```python
'DRIVER={MySQL ODBC 9.3 Unicode Driver};SERVER=localhost;DATABASE=control_inventario;UID=root;PWD=tu_contraseña'
```

4. Ejecutar el proyecto:
```bash
python main.py
```

---

# **Notas finales**

- Todas las consultas SQL son parametrizadas para evitar inyección SQL.  
- Se recomienda cerrar siempre las conexiones a la base de datos para evitar problemas de recursos.  
- El proyecto está estructurado siguiendo el patrón MVC para una mejor organización y mantenimiento del código.
