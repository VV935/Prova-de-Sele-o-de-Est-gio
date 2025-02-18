from pydantic import BaseModel
from typing import Optional

class EmpresaBase(BaseModel):
    id: int
    nome: str
    cnpj: int
    endereco: str
    email: str
    telefone: int

    class Config:
        orm_mode = True

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaResponse(EmpresaBase):
    id: int

class ObrigacaoAcessoriaBase(BaseModel):
    id: int
    nome: str
    periodicidade: str

class ObrigacaoAcessoriaCreate(ObrigacaoAcessoriaBase):
    fk_empresa: int

class ObrigacaoAcessoria(ObrigacaoAcessoriaBase):
    id: int
    fk_empresa: int

    class Config:
        orm_mode = True
