# Control de Inventario MVC

Aplicación web y CLI para gestionar el inventario de productos, construida con el patrón MVC.

## Características

- **Ver todos los productos** del inventario
- **Agregar nuevos productos** al inventario
- **Actualizar productos** (cantidad y precio)
- **Eliminar productos** del inventario
- **Buscar productos** por nombre
- **Filtrar productos** por rango de precios
- **Calcular el valor total** del inventario

---

## Tecnologías

- **Backend:** FastAPI
- **Base de datos:** PostgreSQL (Neon)
- **ORM/Tabla:** psycopg2
- **Templates:** Jinja2
- **Entorno:** python-dotenv

---

## Estructura del proyecto

```
├── app.py              # Aplicación FastAPI (interfaz web)
├── modelo.py           # Conexión y operaciones con PostgreSQL
├── controlador.py     # Lógica de negocio (para CLI)
├── vista.py           # Interfaz de línea de comandos
├── main.py           # Punto de entrada
├── templates/        # Plantillas HTML
│   ├── base.html
│   ├── home.html
│   ├── agregar.html
│   ├── editar.html
│   ├── buscar.html
│   └── filtrar.html
├── static/css/       # Estilos CSS
├── requirements.txt  # Dependencias
└── .env             # Variables de entorno
```

---

## Instalación

```bash
# Crear entorno virtual
python -m venv .venv
.venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
# Crear archivo .env con DATABASE_URL
```

---

## Ejecución

```bash
# Servidor de desarrollo
uvicorn app:app --reload --port 8000

# O directamente
python app.py
```

---

## Rutas disponibles

| Ruta | Método | Descripción |
|------|--------|-------------|
| `/` | GET | Lista todos los productos |
| `/agregar` | GET/POST | Agregar nuevo producto |
| `/editar/{id}` | GET/POST | Editar producto |
| `/eliminar/{id}` | POST | Eliminar producto |
| `/buscar?q=` | GET | Buscar por nombre |
| `/filtrar` | GET | Filtrar por precio |

---

## API del modelo

```python
modelo.obtener_productos()
modelo.agregar_producto(nombre, cantidad, precio)
modelo.actualizar_producto(id_producto, cantidad, precio)
modelo.eliminar_producto(id_producto)
modelo.buscar_producto_por_nombre(nombre)
modelo.filtrar_por_precio(precio_min, precio_max)
modelo.calcular_valor_total()
```

---

## Notas

- Consultas SQL parametrizadas para prevenir inyección SQL
- Conexión a PostgreSQL via psycopg2
- Configuración de entorno via `.env`