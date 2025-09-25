from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from app.extensions import db

class AuditLog(db.Model):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, nullable=True)
    acao = Column(String(120), nullable=False)
    detalhes = Column(Text, nullable=True)
    ip_origem = Column(String(45), nullable=True)
    criado_em = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<AuditLog {self.acao} - {self.criado_em}>"
