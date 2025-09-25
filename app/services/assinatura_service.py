from app.repository import assinatura_repo
from datetime import datetime
import hashlib

def assinar_formulario(formulario_preenchido_id: int, usuario_id: int, metodo: str, ip: str, dados_pdf: bytes | None = None):
    hash_documento = hashlib.sha256(dados_pdf or str(datetime.utcnow()).encode()).hexdigest()

    assinatura = assinatura_repo.create_assinatura(
        formulario_preenchido_id=formulario_preenchido_id,
        usuario_id=usuario_id,
        metodo=metodo,
        hash_documento=hash_documento,
        ip_origem=ip,
        arquivo_pdf=None 
    )

    return assinatura