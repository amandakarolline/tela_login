from DAO import *
import bcrypt


class ControllerCadastro:

    @staticmethod
    def sessao():
        return DAOBD.retorna_sessao()

    @staticmethod
    def valida_senha(senha):
        erro_senha = ('A senha deve conter:\n'
                      '8 caracteres\n'
                      '1 letra maiúscula\n'
                      '1 minúscula\n'
                      'Números\n'
                      'Caracter Especial')

        if senha.islower():
            return erro_senha
        elif len(senha) < 8:
            return erro_senha
        elif senha.isalpha():
            return erro_senha
        elif senha.isalnum():
            return erro_senha
        else:
            return senha

    @staticmethod
    def cadastrar_usuario(nome, email, senha):
        if not DAOBD.procurar_email_usuario(email):
            situacao_senha = ControllerCadastro.valida_senha(senha)
            if situacao_senha == senha:
                senha_encriptada = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
                DAOBD.salvar_usuario(nome, email, senha_encriptada)
                return "Usuário cadastrado com sucesso!"
            else:
                return situacao_senha
        else:
            return 'Email já cadastrado!'

    @staticmethod
    def login(email, senha):
        email = email.strip().lower()
        if not DAOBD.procurar_email_usuario(email):
            return 'Email não cadastrado'
        elif DAOBD.autenticar_senha(email, senha):
            usuario = DAOBD.procurar_email_usuario(email)
            return usuario
        else:
            return "Senha inválida"

    @staticmethod
    def alterar_senha(email, senha_nova):
        situacao_senha = ControllerCadastro.valida_senha(senha_nova)
        if situacao_senha == senha_nova:
            email = email.strip().lower()
            senha_encriptada = bcrypt.hashpw(senha_nova.encode('utf-8'), bcrypt.gensalt())
            DAOBD.alterar_senha(email, senha_encriptada)
            return 'Senha Alterada'
        else:
            return situacao_senha

    @staticmethod
    def alterar_email(email, novo_email):
        email = email.strip().lower()
        novo_email = novo_email.strip().lower()
        if not DAOBD.procurar_email_usuario(novo_email):
            DAOBD.alterar_email(email, novo_email)
            return 'Email alterado com sucesso!'
        else:
            return "Email já cadastrado!"

    @staticmethod
    def alterar_nome(email, novo_nome):
        email = email.strip().lower()
        DAOBD.alterar_nome(email, novo_nome)
        return 'Nome alterado com sucesso!'
