"""
Este módulo define los modelos de datos para la aplicación FastAPI.
"""

from pydantic import BaseModel

class Item(BaseModel):
    """
    Representa un artículo con un nombre y un precio.
    Este modelo puede ser utilizado para la validación de entrada
    y serialización de salida en los endpoints de la API.
    """
    name: str
    price: float
    description: str | None = None
    tax: float | None = None
