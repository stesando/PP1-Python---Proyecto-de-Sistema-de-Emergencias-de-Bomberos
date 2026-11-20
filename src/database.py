
from pathlib import Path

from sqlmodel import SQLModel, Session, create_engine

# Ruta de la base de datos SQLite
BASE_DIR = Path(__file__).resolve().parent
DATABASE_URL = f"sqlite:///{BASE_DIR / 'emergencias.db'}"

# Motor de conexión
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Dependencia para FastAPI
def get_db():
    with Session(engine) as session:
        yield session
