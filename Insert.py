from database import SessionLocal
from models import Empresa, ObrigacaoAcessoria

# Criando uma sessão do banco
db = SessionLocal()

# Inserir uma nova empresa
new_empresa = Empresa(
    id= 10101158,
    nome="Empresa Teste",
    cnpj="12345678000158",
    endereco="Rua Teste, 123",
    email="empresa@teste.com",
    telefone=1234567890
)
db.add(new_empresa)
db.commit()
db.refresh(new_empresa)

print(f"Empresa criada: {new_empresa.nome}")

# Consultar a empresa criada
empresa = db.query(Empresa).filter(Empresa.id == new_empresa.id).first()
if empresa:
    print(f"Empresa encontrada: {empresa.nome}")
else:
    print("Empresa não encontrada.")

# Criar uma obrigação acessória para essa empresa
new_obrigacao = ObrigacaoAcessoria(
    id=10101158,
    nome="Declaração de Impostos",
    periodicidade="mensal",
    fk_empresa=new_empresa.id
)
db.add(new_obrigacao)
db.commit()
db.refresh(new_obrigacao)

print(f"Obrigação criada: {new_obrigacao.nome}")

# Fechar a sessão
db.close()
