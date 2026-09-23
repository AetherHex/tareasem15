import uuid

from pydantic import Field
from pydantic.dataclasses import dataclass


@dataclass
class Producto:
    nombre: str
    stock: int
    precio: float
    # parametros automaticos
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
