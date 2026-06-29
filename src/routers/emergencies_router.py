from fastapi import APIRouter, HTTPException, Path, Query
from typing import Annotated

from models.emergency_model import Emergency, EmergencyUpdate

router = APIRouter()

emergencies = [

    {
        "id": 1,
        "caller_name": "Juan Perez",
        "location": "Ruta 8 km 600",
        "emergency_type": "Incendio Estructural",
        "status": "En camino",
        "unit": "Autobomba 23"
    }

]


@router.get(
    "/emergencias",
    response_model=list[Emergency],
    tags=["Emergencias"],
    summary="Obtener todas las emergencias",
    description="Devuelve la lista completa de emergencias registradas"
)
def get_emergencies():
    return emergencies


@router.get(
    "/emergencias/{emergency_id}",
    response_model=Emergency,
    tags=["Emergencias"],
    summary="Buscar emergencia por ID",
    description="Obtiene una emergencia específica según su identificador",
)
def get_emergency(

    emergency_id: Annotated[
        int,
        Path(gt=0)
    ]

):

    for emergency in emergencies:

        if emergency["id"] == emergency_id:
            return emergency

    raise HTTPException(
        status_code=404,
        detail="Emergencia no encontrada"
    )


@router.get(
    "/emergencias/buscar/",
    tags=["Emergencias"],
    summary="Buscar emergencias por estado",
    description="Permite filtrar emergencias según su estado operativo",
    response_model=list[Emergency]
)
def search_emergency(

    status: Annotated[
        str,
        Query(description="Buscar por estado")
    ]

):

    results = []

    for emergency in emergencies:

        if emergency["status"].lower() == status.lower():
            results.append(emergency)

    return results


@router.post(
    "/emergencias",
    response_model=Emergency,
    tags=["Emergencias"],
    summary="Registrar emergencia",
    description="Crea una nueva emergencia en el sistema",
)
def create_emergency(emergency: Emergency):

    emergencies.append(emergency.model_dump())

    return emergency


@router.put(
    "/emergencias/{emergency_id}",
    tags=["Emergencias"],
    summary="Actualizar emergencia",
    description="Actualiza los datos de una emergencia existente",
    response_model=Emergency,
    responses={404: {"description": "Emergencia no encontrada"}}
)
def update_emergency(

    emergency_id: Annotated[
        int,
        Path(gt=0)
    ],

    emergency_data: EmergencyUpdate

):

    for emergency in emergencies:

        if emergency["id"] == emergency_id:

            emergency["caller_name"] = emergency_data.caller_name
            emergency["location"] = emergency_data.location
            emergency["emergency_type"] = emergency_data.emergency_type
            emergency["status"] = emergency_data.status
            emergency["unit"] = emergency_data.unit

            return emergency

    raise HTTPException(
        status_code=404,
        detail="Emergencia no encontrada"
    )


@router.delete(
  "/emergencias/{emergency_id}",
    tags=["Emergencias"],
    summary="Eliminar emergencia",
    description="Elimina una emergencia específica del sistema",
    responses={404: {"description": "Emergencia no encontrada"}}
)
def delete_emergency(

    emergency_id: Annotated[
        int,
        Path(gt=0)
    ]

):

    for emergency in emergencies:

        if emergency["id"] == emergency_id:

            emergencies.remove(emergency)

            return {
                "message": "Emergencia eliminada"
            }

    raise HTTPException(
        status_code=404,
        detail="Emergencia no encontrada"
    )