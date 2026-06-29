from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.emergencies_router import router as emergencies_router

app = FastAPI(

    title="Sistema de Gestión de Bomberos 🚒",

    description="""
API para administrar emergencias de bomberos.

Permite:

- Registrar pedidos de auxilio
- Consultar emergencias
- Actualizar estados operativos
- Eliminar registros
- Gestionar unidades móviles
""",

    version="1.0"
)

# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Router

app.include_router(emergencies_router)


@app.get("/", tags=["Inicio"])
def inicio():

    return {
        "mensaje": "Sistema de Bomberos funcionando 🚒"
    }