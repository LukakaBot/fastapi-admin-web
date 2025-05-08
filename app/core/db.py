from sqlalchemy import Engine
from sqlmodel import create_engine, SQLModel
from app.core.config import settings

engine: Engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))
