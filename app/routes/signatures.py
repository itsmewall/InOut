from flask import request, jsonify, session
from app.routes import signatures_bp
from app.repository import assinatura_repo

@signatures_bp.route("/sign/<int:formulario_preenchido_id>", methods=["POST"])
def sign_document(formulario_preenchido_id):
    user_id = session.get("user_id")
    metodo = request.json.get("metodo", "aceite_simples")
    hash_documento = request.json.get("hash_documento")

    assinatura = assinatura_repo.create_assinatura(
        formulario_preenchido_id=formulario_preenchido_id,
        usuario_id=user_id,
        metodo=metodo,
        hash_documento=hash_documento,
        ip_origem=request.remote_addr
    )
    return jsonify({"status": "ok", "assinatura_id": assinatura.id})