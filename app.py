from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from modelo import ModeloInventario
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Control de Inventario")

static_dir = os.path.join(os.path.dirname(__file__), "static")
templates_dir = os.path.join(os.path.dirname(__file__), "templates")

if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

templates = Jinja2Templates(directory=templates_dir)

modelo = ModeloInventario()


@app.get("/", name="home")
async def home(request: Request):
    productos = modelo.obtener_productos()
    valor_total = modelo.calcular_valor_total()
    return templates.TemplateResponse("home.html", {
        "request": request,
        "productos": productos,
        "valor_total": valor_total
    })


@app.get("/agregar", name="agregar")
async def mostrar_agregar(request: Request):
    return templates.TemplateResponse("agregar.html", {"request": request})


@app.post("/agregar", name="agregar_post")
async def agregar_producto(request: Request):
    form = await request.form()
    nombre = form.get("nombre")
    cantidad = int(form.get("cantidad"))
    precio = float(form.get("precio"))

    if modelo.agregar_producto(nombre, cantidad, precio):
        return RedirectResponse(url="/", status_code=303)
    else:
        raise HTTPException(status_code=500, detail="Error al agregar producto")


@app.get("/editar/{id_producto}", name="editar")
async def mostrar_editar(request: Request, id_producto: int):
    productos = modelo.obtener_productos()
    producto = next((p for p in productos if p[0] == id_producto), None)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return templates.TemplateResponse("editar.html", {
        "request": request,
        "producto": producto
    })


@app.post("/editar/{id_producto}", name="editar_post")
async def editar_producto(request: Request, id_producto: int):
    form = await request.form()
    cantidad = int(form.get("cantidad"))
    precio = float(form.get("precio"))

    if modelo.actualizar_producto(id_producto, cantidad, precio):
        return RedirectResponse(url="/", status_code=303)
    else:
        raise HTTPException(status_code=500, detail="Error al actualizar producto")


@app.post("/eliminar/{id_producto}", name="eliminar")
async def eliminar_producto(id_producto: int):
    if modelo.eliminar_producto(id_producto):
        return RedirectResponse(url="/", status_code=303)
    else:
        raise HTTPException(status_code=500, detail="Error al eliminar producto")


@app.get("/buscar", name="buscar")
async def mostrar_buscar(request: Request, q: str = ""):
    if q:
        productos = modelo.buscar_producto_por_nombre(q)
    else:
        productos = []
    return templates.TemplateResponse("buscar.html", {
        "request": request,
        "productos": productos,
        "q": q
    })


@app.get("/filtrar", name="filtrar")
async def mostrar_filtrar(request: Request, min_price: float = 0, max_price: float = 999999):
    productos = modelo.filtrar_por_precio(min_price, max_price)
    return templates.TemplateResponse("filtrar.html", {
        "request": request,
        "productos": productos,
        "min_price": min_price,
        "max_price": max_price
    })


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
