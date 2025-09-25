from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.extensions import db

class Assinatura(db.Model):
    __tablename__ = "assinaturas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    formulario_preenchido_id = Column(Integer, ForeignKey("formularios_preenchidos.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    metodo = Column(String(50), nullable=False)  # govbr, icp, aceite_simples
    hash_documento = Column(String(255), nullable=False)
    ip_origem = Column(String(45), nullable=True)  # IPv4/IPv6
    arquivo_pdf = Column(String(255), nullable=True)  # path do arquivo assinado
    criado_em = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("User", back_populates="assinaturas")
    formulario = relationship("FormularioPreenchido", back_populates="assinatura")

    def __repr__(self):
        return f"<Assinatura {self.metodo} por User {self.usuario_id}>"
