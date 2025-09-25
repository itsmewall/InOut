from app.extensions import db
from app.models.empresa import Empresa

def get_empresa_by_id(empresa_id: int) -> Empresa | None:
    return db.session.get(Empresa, empresa_id)

def get_empresa_by_cnpj(cnpj: str) -> Empresa | None:
    return Empresa.query.filter_by(cnpj=cnpj).first()

def create_empresa(nome: str, cnpj: str, tema_css: str = "default.css") -> Empresa:
    empresa = Empresa(nome=nome, cnpj=cnpj, tema_css=tema_css)
    db.session.add(empresa)
    db.session.commit()
    return empresa

def update_empresa(empresa: Empresa, **kwargs) -> Empresa:
    for key, value in kwargs.items():
        setattr(empresa, key, value)
    db.session.commit()
    return empresa

def delete_empresa(empresa: Empresa) -> None:
    db.session.delete(empresa)
    db.session.commit()