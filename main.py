
# main.py
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the FastAPI application
app = FastAPI(
    title="Mi Aplicación FastAPI",
    description="Una API de ejemplo para gestionar datos.",
    version="1.0.0"
)

# Define a Pydantic model for data (example)
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# In-memory database (for demonstration purposes)
db = []

@app.get("/")
async def read_root():
    """
    Endpoint raíz que devuelve un mensaje de bienvenida.
    """
    return {"message": "¡Bienvenido a mi API FastAPI!"}

@app.post("/items/")
async def create_item(item: Item):
    """
    Crea un nuevo ítem en la base de datos.
    """
    db.append(item.model_dump())
    return {"message": "Ítem creado exitosamente", "item": item}

@app.get("/items/")
async def read_items():
    """
    Obtiene todos los ítems almacenados en la base de datos.
    """
    return {"items": db}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Obtiene un ítem específico por su ID.
    """
    if item_id < len(db):
        return {"item": db[item_id]}
    return {"message": "Ítem no encontrado", "item_id": item_id}

