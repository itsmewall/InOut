from flask import render_template, request, redirect, url_for, session
from app.routes import forms_bp
from app.repository import form_repo

@forms_bp.route("/<int:step>", methods=["GET", "POST"])
def form_step(step):
    user_id = session.get("user_id")
    empresa_id = session.get("empresa_id")

    if request.method == "POST":
        dados = dict(request.form)
        form_repo.create_formulario_preenchido(
            formulario_id=step,
            usuario_id=user_id,
            empresa_id=empresa_id,
            dados_json=str(dados)
        )
        return redirect(url_for("forms.form_step", step=step + 1))

    return render_template(f"forms/step{step}.html")