import bcrypt

from model import Usuario
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DAOBD:
    @classmethod
    def retorna_sessao(cls):
        USUARIO = "root"
        SENHA = ""
        HOST = "localhost"
        BANCO = "projeto2login"
        PORT = "3306"

        CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

        engine = create_engine(CONN, echo=True)
        Session = sessionmaker(bind=engine)
        return Session()

    @classmethod
    def salvar_usuario(cls, nome, email, senha):
        session = cls.retorna_sessao()
        usuario = Usuario(nome=nome, email=email, senha=senha)
        session.add(usuario)
        session.commit()

    @classmethod
    def procurar_email_usuario(cls, email):
        session = cls.retorna_sessao()
        usuario = session.query(Usuario).filter_by(email=email).one_or_none()
        return usuario

    @classmethod
    def alterar_senha(cls, email, senha_nova):
        session = cls.retorna_sessao()
        usuario = session.query(Usuario).filter_by(email=email).one_or_none()
        usuario.senha = senha_nova
        session.commit()

    @classmethod
    def autenticar_senha(cls, email, senha_digitada):
        usuario = cls.procurar_email_usuario(email)
        return bcrypt.checkpw(senha_digitada.encode('utf-8'), usuario.senha.encode('utf-8'))

    @classmethod
    def alterar_email(cls, email, novo_email):
        session = cls.retorna_sessao()
        usuario = session.query(Usuario).filter_by(email=email).one_or_none()
        usuario.email = novo_email
        session.commit()

    @classmethod
    def alterar_nome(cls, email, novo_nome):
        session = cls.retorna_sessao()
        usuario = session.query(Usuario).filter_by(email=email).one_or_none()
        usuario.nome = novo_nome
        session.commit()
