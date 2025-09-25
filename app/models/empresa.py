from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.extensions import db

class Empresa(db.Model):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(120), nullable=False)
    cnpj = Column(String(18), unique=True, nullable=False)
    ativa = Column(Boolean, default=True)
    tema_css = Column(String(255), default="default.css")
    criado_em = Column(DateTime, default=datetime.utcnow)

    usuarios = relationship("User", back_populates="empresa", cascade="all, delete")
    formularios = relationship("FormularioPreenchido", back_populates="empresa")

    def __repr__(self):
        return f"<Empresa {self.nome}>"
