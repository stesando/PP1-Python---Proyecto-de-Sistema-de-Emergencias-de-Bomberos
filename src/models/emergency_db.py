
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class BomberoDB(SQLModel, table=True):
    __tablename__ = "bomberos"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=50)
    apellido: str = Field(max_length=50)
    rango: str = Field(max_length=30)

    emergencias: list["EmergencyDB"] = Relationship(
        back_populates="bombero"
    )


class EmergencyDB(SQLModel, table=True):
    __tablename__ = "emergencias"

    id: Optional[int] = Field(default=None, primary_key=True)
    caller_name: str = Field(max_length=50)
    location: str = Field(max_length=100)
    emergency_type: str = Field(max_length=30)
    status: str
    unit: str = Field(max_length=30)

    bombero_id: Optional[int] = Field(
        default=None,
        foreign_key="bomberos.id"
    )

    bombero: Optional[BomberoDB] = Relationship(
        back_populates="emergencias"
    )
