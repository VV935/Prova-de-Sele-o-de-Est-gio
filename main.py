from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas

# Criar tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência para obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar empresa
@app.post("/empresas/", response_model=schemas.EmpresaBase)
def criar_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    nova_empresa = models.Empresa(**empresa.dict())
    db.add(nova_empresa)
    db.commit()
    db.refresh(nova_empresa)
    return nova_empresa

# Listar empresas
@app.get("/empresas/", response_model=list[schemas.EmpresaBase])
def listar_empresas(db: Session = Depends(get_db)):
    return db.query(models.Empresa).all()

# Criar obrigação acessória
@app.post("/obrigacoes/", response_model=schemas.ObrigacaoAcessoria)
def criar_obrigacao(obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    nova_obrigacao = models.ObrigacaoAcessoria(**obrigacao.dict())
    db.add(nova_obrigacao)
    db.commit()
    db.refresh(nova_obrigacao)
    return nova_obrigacao

