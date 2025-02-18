from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexao com o banco PostgreSQL
DATABASE_URL = "postgresql://postgres:88392071@localhost:5432/Empresas_db"

# engine (conexao)
engine = create_engine(DATABASE_URL, echo=True)

# Base para os modelos
Base = declarative_base()

# sessao
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()


