from app.extensions import db
from app.models.user import User

def get_user_by_id(user_id: int) -> User | None:
    return db.session.get(User, user_id)

def get_user_by_email(email: str) -> User | None:
    return User.query.filter_by(email=email).first()

def get_users_by_empresa(empresa_id: int) -> list[User]:
    return User.query.filter_by(empresa_id=empresa_id).all()

def create_user(empresa_id: int, nome: str, email: str, cpf: str, senha_hash: str | None = None) -> User:
    user = User(empresa_id=empresa_id, nome=nome, email=email, cpf=cpf, senha_hash=senha_hash)
    db.session.add(user)
    db.session.commit()
    return user

def update_user(user: User, **kwargs) -> User:
    for key, value in kwargs.items():
        setattr(user, key, value)
    db.session.commit()
    return user

def delete_user(user: User) -> None:
    db.session.delete(user)
    db.session.commit()