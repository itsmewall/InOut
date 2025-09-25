from app.repository import user_repo, empresa_repo

def criar_usuario(empresa_id: int, nome: str, email: str, cpf: str, senha_hash: str | None = None):
    empresa = empresa_repo.get_empresa_by_id(empresa_id)
    if not empresa or not empresa.ativa:
        raise ValueError("Empresa não encontrada ou inativa")

    return user_repo.create_user(
        empresa_id=empresa.id,
        nome=nome,
        email=email,
        cpf=cpf,
        senha_hash=senha_hash
    )
