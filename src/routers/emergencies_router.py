from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Query
from sqlalchemy.orm import Session

from database import get_db
from models.emergency_model import Emergency, EmergencyUpdate,EmergencyCreate
from models.emergency_db import EmergencyDB

router = APIRouter()


@router.get(
    "/emergencias",
    response_model=list[Emergency],
    tags=["Emergencias"],
    summary="Obtener todas las emergencias",
)
def get_emergencies(db: Session = Depends(get_db)):
    return db.query(EmergencyDB).all()


@router.get(
    "/emergencias/{emergency_id}",
    response_model=Emergency,
    tags=["Emergencias"],
    summary="Buscar emergencia por ID",
)
def get_emergency(
    emergency_id: Annotated[int, Path(gt=0)],
    db: Session = Depends(get_db),
):
    emergency = (
        db.query(EmergencyDB)
        .filter(EmergencyDB.id == emergency_id)
        .first()
    )

    if emergency is None:
        raise HTTPException(
            status_code=404,
            detail="Emergencia no encontrada",
        )

    return emergency


@router.get(
    "/emergencias/buscar/",
    response_model=list[Emergency],
    tags=["Emergencias"],
    summary="Buscar emergencias por estado",
)
def search_emergency(
    status: Annotated[str, Query(description="Buscar por estado")],
    db: Session = Depends(get_db),
):
    return (
        db.query(EmergencyDB)
        .filter(EmergencyDB.status.ilike(status))
        .all()
    )


@router.post(
    "/emergencias",
    response_model=Emergency,
    tags=["Emergencias"],
    summary="Registrar emergencia",
)
def create_emergency(
    emergency: EmergencyCreate,
    db: Session = Depends(get_db),
):
    db_emergency = EmergencyDB(**emergency.model_dump())

    db.add(db_emergency)
    db.commit()
    db.refresh(db_emergency)

    return db_emergency


@router.put(
    "/emergencias/{emergency_id}",
    response_model=Emergency,
    tags=["Emergencias"],
    summary="Actualizar emergencia",
)
def update_emergency(
    emergency_id: Annotated[int, Path(gt=0)],
    emergency_data: EmergencyUpdate,
    db: Session = Depends(get_db),
):
    emergency = (
        db.query(EmergencyDB)
        .filter(EmergencyDB.id == emergency_id)
        .first()
    )

    if emergency is None:
        raise HTTPException(
            status_code=404,
            detail="Emergencia no encontrada",
        )

    for field, value in emergency_data.model_dump().items():
        setattr(emergency, field, value)

    db.commit()
    db.refresh(emergency)

    return emergency


@router.delete(
    "/emergencias/{emergency_id}",
    tags=["Emergencias"],
    summary="Eliminar emergencia",
)
def delete_emergency(
    emergency_id: Annotated[int, Path(gt=0)],
    db: Session = Depends(get_db),
):
    emergency = (
        db.query(EmergencyDB)
        .filter(EmergencyDB.id == emergency_id)
        .first()
    )

    if emergency is None:
        raise HTTPException(
            status_code=404,
            detail="Emergencia no encontrada",
        )

    db.delete(emergency)
    db.commit()

    return {"message": "Emergencia eliminada"}
