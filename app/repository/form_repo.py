from app.extensions import db
from app.models.form import Formulario, FormularioPreenchido

# Catálogo de formulários
def get_all_formularios() -> list[Formulario]:
    return Formulario.query.all()

def get_formulario_by_id(formulario_id: int) -> Formulario | None:
    return db.session.get(Formulario, formulario_id)

# Formulários preenchidos
def create_formulario_preenchido(formulario_id: int, usuario_id: int, empresa_id: int, dados_json: str) -> FormularioPreenchido:
    preenchido = FormularioPreenchido(
        formulario_id=formulario_id,
        usuario_id=usuario_id,
        empresa_id=empresa_id,
        dados_json=dados_json
    )
    db.session.add(preenchido)
    db.session.commit()
    return preenchido

def get_formularios_preenchidos_by_usuario(usuario_id: int) -> list[FormularioPreenchido]:
    return FormularioPreenchido.query.filter_by(usuario_id=usuario_id).all()

def get_formulario_preenchido_by_id(preenchido_id: int) -> FormularioPreenchido | None:
    return db.session.get(FormularioPreenchido, preenchido_id)