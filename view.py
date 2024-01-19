import controller

if __name__ == '__main__':
    while True:
        cat = controller.ControllerCadastro()
        local = int(input('Digite 1 para criar novo usuário\n'
                          'Digite 2 para fazer login\n'
                          'Digite 3 para sair\n'))

        match local:
            case 1:
                nome = input('Digite seu nome: ')
                email = input('Digite seu email: ')
                senha = input('Digite sua senha: ')
                print(cat.cadastrar_usuario(nome, email, senha))

            case 2:
                email = input('Digite seu email: ')
                senha = input('Digite sua senha: ')
                print(cat.login(email, senha))

                while True:
                    decisao = int(input("Digite 1 para alterar senha\n"
                                        "Digite 2 para alterar email\n"
                                        "Digite 3 para alterar nome\n"
                                        "Digite 4 para deslogar\n"))

                    match decisao:
                        case 1:
                            nova_senha = input('Digite a nova senha: ')
                            print(cat.alterar_senha(email, nova_senha))

                        case 2:
                            novo_email = input('Digite o novo email: ')
                            print(cat.alterar_email(email, novo_email))

                        case 3:
                            novo_nome = input('Digite o novo nome: ')
                            print(cat.alterar_nome(email, novo_nome))

                        case 4:
                            break

            case 3:
                break
