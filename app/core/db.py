from sqlalchemy import Engine
from sqlmodel import create_engine, SQLModel
from app.core.config import settings

engine: Engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

# 创建数据库表
SQLModel.metadata.create_all(engine)
