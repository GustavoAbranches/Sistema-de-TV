from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from src.models.usuario_model import User, db

bcrypt = Bcrypt()

# Criar um novo usuário no banco de dados
def criar_usuario(nome, email, senha, role, setor=None):
    if User.query.filter_by(email=email).first():
        return None
    user = User(
        nome=nome,
        email=email,
        role=role,
        setor=setor
    )
    user.senha_hash = bcrypt.generate_password_hash(senha).decode('utf-8')
    db.session.add(user)
    db.session.commit()
    return user

# Verifica se as credenciais estão corretas
def verificar_usuario(email, senha):
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.senha_hash, senha):
        return user
    return None

# Gera um JWT com informações do usuário
def gerar_token(user):
    additional_claims = {
        'role': user.role,
        'setor': user.setor
    }
    return create_access_token(identity=str(user.id), additional_claims=additional_claims)

# Lista todos os usuários (apenas para superadmin)
def listar_usuarios():
    return User.query.all()