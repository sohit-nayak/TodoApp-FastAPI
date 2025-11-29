from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp_deployment.db"

SQLALCHEMY_DATABASE_URL = "postgresql://todoapp_eryy_user:ykpTeyVSoUAJ0ZR4f0oWreSgUtuWd35l@dpg-d4lj3h8gjchc73aooohg-a/todoapp_eryy"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



