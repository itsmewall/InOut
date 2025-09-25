from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.extensions import db

class Formulario(db.Model):
    __tablename__ = "formularios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(120), nullable=False)
    descricao = Column(Text, nullable=True)
    ativo = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Formulario {self.nome}>"


class FormularioPreenchido(db.Model):
    __tablename__ = "formularios_preenchidos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    formulario_id = Column(Integer, ForeignKey("formularios.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False)
    dados_json = Column(Text, nullable=False)  # respostas salvas em JSON
    criado_em = Column(DateTime, default=datetime.utcnow)

    formulario = relationship("Formulario")
    usuario = relationship("User", back_populates="formularios")
    empresa = relationship("Empresa", back_populates="formularios")
    assinatura = relationship("Assinatura", uselist=False, back_populates="formulario")

    def __repr__(self):
        return f"<FormularioPreenchido {self.formulario_id} - Usuario {self.usuario_id}>"
