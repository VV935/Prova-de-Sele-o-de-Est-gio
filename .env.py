from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL=postgresql://postgres:88392071@localhost:5432/Empresas_db

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Recuperar a URL do banco de dados do .env
SQLALCHEMY_DATABASE_URL = os.getenv("DB_URL")

# Criando a engine do SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Criando a base para os modelos
Base = declarative_base()

# Criando a sessao
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()

