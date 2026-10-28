

from sqlalchemy import Column, Integer, String

from database import Base


class EmergencyDB(Base):
    __tablename__ = "emergencias"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    caller_name = Column(String(50), nullable=False)
    location = Column(String(100), nullable=False)
    emergency_type = Column(String(30), nullable=False)
    status = Column(String, nullable=False)
    unit = Column(String(30), nullable=False)
