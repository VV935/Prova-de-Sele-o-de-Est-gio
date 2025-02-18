from sqlalchemy.orm import Session
from models import Empresa, ObrigacaoAcessoria
from database import SessionLocal

def create_obrigacao(db: Session, id: int, nome: str, periodicidade: str, fk_empresa: int):
    db_obrigacao = ObrigacaoAcessoria(nome=nome, periodicidade=periodicidade, fk_empresa=fk_empresa)
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

# Criando uma sessão e utilizando a função para criar uma obrigação
db = SessionLocal()
create_obrigacao(db, "1", "Declaração de Impostos", "mensal", 1)  # Aqui você passa o ID da empresa
