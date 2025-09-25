from flask import render_template, session
from app.routes import dashboard_bp
from app.repository import user_repo, form_repo

@dashboard_bp.route("/")
def index():
    empresa_id = session.get("empresa_id")
    usuarios = user_repo.get_users_by_empresa(empresa_id)
    formularios = form_repo.get_all_formularios()
    return render_template("dashboard/index.html", usuarios=usuarios, formularios=formularios)