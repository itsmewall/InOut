from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.extensions import db

class User(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False)
    nome = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    cpf = Column(String(14), unique=True, nullable=False)
    senha_hash = Column(String(255), nullable=True)  # se não usar Gov.br
    ativo = Column(Boolean, default=True)
    criado_em = Column(DateTime, default=datetime.utcnow)

    empresa = relationship("Empresa", back_populates="usuarios")
    formularios = relationship("FormularioPreenchido", back_populates="usuario")
    assinaturas = relationship("Assinatura", back_populates="usuario")

    def __repr__(self):
        return f"<User {self.nome} ({self.email})>"
