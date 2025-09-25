from flask import Blueprint

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
users_bp = Blueprint("users", __name__, url_prefix="/users")
forms_bp = Blueprint("forms", __name__, url_prefix="/forms")
signatures_bp = Blueprint("signatures", __name__, url_prefix="/signatures")
dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

# Importa rotas
from app.routes import auth, users, forms, signatures, dashboard