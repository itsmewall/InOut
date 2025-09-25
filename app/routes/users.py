from flask import render_template, request, redirect, url_for, session
from app.routes import users_bp
from app.repository import user_repo

@users_bp.route("/")
def list_users():
    empresa_id = session.get("empresa_id")
    users = user_repo.get_users_by_empresa(empresa_id)
    return render_template("dashboard/usuarios.html", users=users)

@users_bp.route("/create", methods=["POST"])
def create_user():
    empresa_id = session.get("empresa_id")
    data = request.form
    user_repo.create_user(
        empresa_id=empresa_id,
        nome=data["nome"],
        email=data["email"],
        cpf=data["cpf"]
    )
    return redirect(url_for("users.list_users"))

@users_bp.route("/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):
    user = user_repo.get_user_by_id(user_id)
    if user:
        user_repo.delete_user(user)
    return redirect(url_for("users.list_users"))