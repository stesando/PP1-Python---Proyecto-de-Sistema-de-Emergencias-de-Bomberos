from pydantic import BaseModel, Field
from typing import Annotated


class Emergency(BaseModel):

    id: Annotated[
        int,
        Field(gt=0, description="ID de la emergencia")
    ]

    caller_name: Annotated[
        str,
        Field(min_length=3, max_length=50)
    ]

    location: Annotated[
        str,
        Field(min_length=5, max_length=100)
    ]

    emergency_type: Annotated[
        str,
        Field(min_length=3, max_length=30)
    ]

    status: Annotated[
        str,
        Field(description="Estado de la emergencia")
    ]

    unit: Annotated[
        str,
        Field(min_length=2, max_length=30)
    ]


class EmergencyUpdate(BaseModel):

    caller_name: Annotated[
        str,
        Field(min_length=3, max_length=50)
    ]

    location: Annotated[
        str,
        Field(min_length=5, max_length=100)
    ]

    emergency_type: Annotated[
        str,
        Field(min_length=3, max_length=30)
    ]

    status: Annotated[
        str,
        Field(description="Estado de la emergencia")
    ]

    unit: Annotated[
        str,
        Field(min_length=2, max_length=30)
    ]