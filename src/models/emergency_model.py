
from typing import Optional
from sqlmodel import SQLModel


# Schema para crear un bombero
class BomberoCreate(SQLModel):
    nombre: str
    apellido: str
    rango: str


# Schema para mostrar un bombero
class BomberoRead(SQLModel):
    id: int
    nombre: str
    apellido: str
    rango: str


# Datos básicos de una emergencia
class EmergencyBase(SQLModel):
    caller_name: str
    location: str
    emergency_type: str
    status: str
    unit: str


# Schema para crear una emergencia
class EmergencyCreate(EmergencyBase):
    bombero_id: Optional[int] = None


# Schema para actualizar una emergencia
class EmergencyUpdate(SQLModel):
    caller_name: Optional[str] = None
    location: Optional[str] = None
    emergency_type: Optional[str] = None
    status: Optional[str] = None
    unit: Optional[str] = None
    bombero_id: Optional[int] = None


# Schema de respuesta con datos anidados
class Emergency(EmergencyBase):
    id: int
    bombero_id: Optional[int] = None
    bombero: Optional[BomberoRead] = None
