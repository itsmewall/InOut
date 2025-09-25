from app.extensions import db
from app.models.assinatura import Assinatura

def create_assinatura(formulario_preenchido_id: int, usuario_id: int, metodo: str, hash_documento: str, ip_origem: str | None = None, arquivo_pdf: str | None = None) -> Assinatura:
    assinatura = Assinatura(
        formulario_preenchido_id=formulario_preenchido_id,
        usuario_id=usuario_id,
        metodo=metodo,
        hash_documento=hash_documento,
        ip_origem=ip_origem,
        arquivo_pdf=arquivo_pdf
    )
    db.session.add(assinatura)
    db.session.commit()
    return assinatura

def get_assinatura_by_id(assinatura_id: int) -> Assinatura | None:
    return db.session.get(Assinatura, assinatura_id)

def get_assinaturas_by_usuario(usuario_id: int) -> list[Assinatura]:
    return Assinatura.query.filter_by(usuario_id=usuario_id).all()

def update_assinatura(assinatura: Assinatura, **kwargs) -> Assinatura:
    for key, value in kwargs.items():
        setattr(assinatura, key, value)
    db.session.commit()
    return assinatura

def delete_assinatura(assinatura: Assinatura) -> None:
    db.session.delete(assinatura)
    db.session.commit()