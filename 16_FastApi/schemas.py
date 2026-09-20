from pydantic import BaseModel, Field, field_validator
from typing import Literal


class TareaCrear(BaseModel):
    titulo: str = Field(min_length=3)
    prioridad: Literal["alta", "media", "baja"]

    @field_validator("titulo")
    def validar_campo(cls, valor):
        if valor.strip() == "":
            raise ValueError("El titulo no es valido")
        return valor

class TareaRespuesta(BaseModel):
    id: int
    titulo: str
    prioridad: Literal["alta", "media", "baja"]

class TareaActualizar(BaseModel):
    titulo: str | None = None
    prioridad: Literal["alta", "media", "baja"] | None = None
    @field_validator("titulo")
    def validar_campo(cls, valor):
        if valor is not None and valor.strip() == "":
            raise ValueError("El titulo no es valido")
        return valor