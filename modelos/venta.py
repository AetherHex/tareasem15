import uuid
from datetime import datetime
from zoneinfo import ZoneInfo

from pydantic import Field
from pydantic.dataclasses import dataclass


@dataclass
class Venta:
    id_producto: str
    id_usuario: str
    cantidad: int
    # automaticos
    fecha: str = Field(
        default_factory=lambda: datetime.now(ZoneInfo("America/Guayaquil")).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    )
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
