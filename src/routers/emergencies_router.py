
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Query
from sqlmodel import Session, select

from database import get_db
from models.emergency_model import (
    Emergency,
    EmergencyCreate,
    EmergencyUpdate,
    BomberoCreate,
    BomberoRead,
)
from models.emergency_db import BomberoDB, EmergencyDB


router = APIRouter()


# Registrar un bombero
@router.post(
    "/bomberos",
    response_model=BomberoRead,
    tags=["Bomberos"]
)
def create_bombero(
    bombero: BomberoCreate,
    db: Session = Depends(get_db)
):
    db_bombero = BomberoDB(**bombero.model_dump())

    db.add(db_bombero)
    db.commit()
    db.refresh(db_bombero)

    return db_bombero


# Obtener todas las emergencias
@router.get(
    "/emergencias",
    response_model=list[Emergency],
    tags=["Emergencias"]
)
def get_emergencies(db: Session = Depends(get_db)):
    statement = select(EmergencyDB)
    emergencies = db.exec(statement).all()

    # Cargar los datos del bombero relacionado
    for emergency in emergencies:
        _ = emergency.bombero

    return emergencies


# Buscar emergencias por estado
@router.get(
    "/emergencias/buscar/",
    response_model=list[Emergency],
    tags=["Emergencias"]
)
def search_emergency(
    status: Annotated[str, Query(description="Buscar por estado")],
    db: Session = Depends(get_db)
):
    statement = select(EmergencyDB).where(
        EmergencyDB.status.ilike(status)
    )

    emergencies = db.exec(statement).all()

    for emergency in emergencies:
        _ = emergency.bombero

    return emergencies


# Buscar emergencia por ID
@router.get(
    "/emergencias/{emergency_id}",
    response_model=Emergency,
    tags=["Emergencias"]
)
def get_emergency(
    emergency_id: Annotated[int, Path(gt=0)],
    db: Session = Depends(get_db)
):
    statement = select(EmergencyDB).where(
        EmergencyDB.id == emergency_id
    )

    emergency = db.exec(statement).first()

    if emergency is None:
        raise HTTPException(
            status_code=404,
            detail="Emergencia no encontrada"
        )

    _ = emergency.bombero

    return emergency


# Registrar emergencia
@router.post(
    "/emergencias",
    response_model=Emergency,
    tags=["Emergencias"]
)
def create_emergency(
    emergency: EmergencyCreate,
    db: Session = Depends(get_db)
):
    db_emergency = EmergencyDB(**emergency.model_dump())

    db.add(db_emergency)
    db.commit()
    db.refresh(db_emergency)

    _ = db_emergency.bombero

    return db_emergency


# Actualizar emergencia
@router.put(
    "/emergencias/{emergency_id}",
    response_model=Emergency,
    tags=["Emergencias"]
)
def update_emergency(
    emergency_id: Annotated[int, Path(gt=0)],
    emergency_data: EmergencyUpdate,
    db: Session = Depends(get_db)
):
    statement = select(EmergencyDB).where(
        EmergencyDB.id == emergency_id
    )

    emergency = db.exec(statement).first()

    if emergency is None:
        raise HTTPException(
            status_code=404,
            detail="Emergencia no encontrada"
        )

    update_data = emergency_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(emergency, field, value)

    db.add(emergency)
    db.commit()
    db.refresh(emergency)

    _ = emergency.bombero

    return emergency


# Eliminar emergencia
@router.delete(
    "/emergencias/{emergency_id}",
    tags=["Emergencias"]
)
def delete_emergency(
    emergency_id: Annotated[int, Path(gt=0)],
    db: Session = Depends(get_db)
):
    statement = select(EmergencyDB).where(
        EmergencyDB.id == emergency_id
    )

    emergency = db.exec(statement).first()

    if emergency is None:
        raise HTTPException(
            status_code=404,
            detail="Emergencia no encontrada"
        )

    db.delete(emergency)
    db.commit()

    return {"message": "Emergencia eliminada"}
