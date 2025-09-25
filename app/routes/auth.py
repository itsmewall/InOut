from flask import redirect, url_for, session, request, render_template
from app.routes import auth_bp
from app.repository import user_repo, empresa_repo
from app.extensions import db

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        cpf = request.form.get("cpf")

        user = user_repo.get_user_by_email(email)
        if user and user.cpf == cpf:
            session["user_id"] = user.id
            session["empresa_id"] = user.empresa_id
            return redirect(url_for("dashboard.index"))

        return render_template("auth/login.html", error="Credenciais inválidas")

    return render_template("auth/login.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
