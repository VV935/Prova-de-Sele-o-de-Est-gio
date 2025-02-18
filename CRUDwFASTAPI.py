from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import EmpresaResponse
from schemas import EmpresaCreate, EmpresaResponse
from sqlalchemy.exc import IntegrityError

app = FastAPI()

# Dependência para obter a sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD - Criar Empresa
@router.post("/empresas/", status_code=201)
def create_empresa(empresa: EmpresaBase, db: Session = Depends(get_db)):
    new_empresa = Empresa(**empresa.model_dump()) 
    db.add(new_empresa)
    db.commit()
    db.refresh(new_empresa)
    return new_empresa

# CRUD - Ler Empresa
@app.get("/empresas/{empresa_id}", response_model=Empresa)
def read_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return db_empresa

@app.post("/obrigacao_acessoria/", response_model=ObrigacaoAcessoria)
def create_obrigacao_acessoria(obrigacao: ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    db_obrigacao = ObrigacaoAcessoria(nome=obrigacao.nome, periodicidade=obrigacao.periodicidade, empresa_id=obrigacao.empresa_id)
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

@app.get("/obrigacao_acessoria/{obrigacao_id}", response_model=ObrigacaoAcessoria)
def read_obrigacao_acessoria(obrigacao_id: int, db: Session = Depends(get_db)):
    db_obrigacao = db.query(ObrigacaoAcessoria).filter(ObrigacaoAcessoria.id == obrigacao_id).first()
    if db_obrigacao is None:
        raise HTTPException(status_code=404, detail="Obrigação de assessoria não encontrada")
    return db_obrigacao
