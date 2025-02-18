from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class ObrigacaoAcessoria(Base):
    __tablename__ = "tb_ObrigacaoAcessoria" 

    id = Column(Integer, primary_key=True, autoincrement=True)  
    nome = Column(String(25), nullable=False)
    periodicidade = Column(String(10), nullable=False)  
    fk_empresa = Column(Integer, ForeignKey("tb_Empresa.id"), nullable=False)  # FK para tb_Empresa

    # Relacionamento com a tabela Empresa (muitos-para-um)
    empresa = relationship("Empresa", back_populates="obrigacoes")

class Empresa(Base):
    __tablename__ = "tb_Empresa" 

    id = Column(Integer, primary_key=True, autoincrement=True)  
    nome = Column(String(25), nullable=False)
    cnpj = Column(String(14), unique=True, nullable=False)
    endereco = Column(String(50), nullable=False)
    email = Column(String(40), nullable=False)
    telefone = Column(Integer, nullable=False)

    # Relacionamento com a tabela ObrigacaoAcessoria (um-para-muitos)
    obrigacoes = relationship("ObrigacaoAcessoria", back_populates="empresa")