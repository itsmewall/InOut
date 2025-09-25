from app.repository import empresa_repo

def get_theme_for_empresa(empresa_id: int) -> dict:
    empresa = empresa_repo.get_empresa_by_id(empresa_id)
    if not empresa:
        return {"css": "default.css", "logo": "default.png"}

    return {"css": empresa.tema_css, "logo": f"logos/{empresa.id}.png"}
