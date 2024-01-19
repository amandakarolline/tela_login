import flet as ft
import controller
import time

cat = controller.ControllerCadastro()


def main(page: ft.Page):
    email = None
    dlg = None
    # Configuração da página
    page.title = 'Login Screen'
    page.window_width = 600
    page.window_height = 600
    page.window_resizable = False
    page.padding = 100
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def alerta(msg):
        page.add(msg)
        page.update()
        time.sleep(1)
        page.remove(msg)
        page.update()

    def limpar_campos():
        nome_input.value = ''
        pass_input.value = ''

    def validar_campos():
        return all([email_input.value, pass_input.value])

    def exibir_mensagem_erro(entrada):
        msg = ft.Text(entrada, style=ft.TextThemeStyle.LABEL_MEDIUM, color='red')
        alerta(msg)

    def realizar_login():
        nonlocal email
        entrada = cat.login(email_input.value, pass_input.value)
        if entrada in ["Senha inválida", 'Email não cadastrado']:
            exibir_mensagem_erro(entrada)
        else:
            limpar_campos()
            page.remove(login)
            usuario = entrada
            email = usuario.email
            page.title = 'Administrar Cadastro'
            page.appbar = ft.AppBar(title=ft.Text(f'Bem-Vindo(a) {usuario.nome}'), center_title=True)
            page.add(alteracoes)

    # Função chamada quando o botão é clicado
    def btn_login(e):
        if validar_campos():
            realizar_login()
        else:
            exibir_mensagem_erro("Preencha todos os campos")

    def btn_cadastro(e):
        page.remove(login)
        page.title = 'Cadastro'
        page.appbar = ft.AppBar(title=ft.Text('Cadastro'), center_title=True)
        limpar_campos()
        email_input.value = ''
        page.add(cadastro)

    def btn_submeter_cadastro(e):
        if all([nome_input.value, email_input.value, pass_input.value]):
            nonlocal dlg
            cadastro = cat.cadastrar_usuario(nome_input.value, email_input.value, pass_input.value)

            dlg = ft.AlertDialog(
                title=ft.Text(cadastro),
                actions=[ok_btn],
                actions_alignment=ft.MainAxisAlignment.END)
            page.dialog = dlg

            def on_ok_click(e):
                close_dlg()
                page.update()

            ok_btn.on_click = on_ok_click

            dlg.open = True
            page.update()

    def close_dlg():
        dlg.open = False

    def confirmar_alteracao_senha():
        if all([pass_input.value]):
            entrada = cat.alterar_senha(email, pass_input.value)
            exibir_mensagem_erro(entrada)
        close_dlg()

    def confirmar_alteracao_nome():
        if all([nome_input.value]):
            entrada = cat.alterar_nome(email, nome_input.value)
            exibir_mensagem_erro(entrada)
        close_dlg()

    def confirmar_alteracao_email():
        if all([email_input.value]):
            entrada = cat.alterar_email(email, email_input.value)
            exibir_mensagem_erro(entrada)
        close_dlg()

    def btn_alterar_senha(e):
        open_dialog("Digite uma nova senha", pass_input, confirmar_alteracao_senha)

    def btn_alterar_nome(e):
        open_dialog("Digite o novo nome", nome_input, confirmar_alteracao_nome)

    def btn_alterar_email(e):
        open_dialog("Digite um novo email", email_input, confirmar_alteracao_email)

    def open_dialog(title, content, confirm_callback):
        nonlocal dlg
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text(title),
            content=content,
            actions=[cancel_btn, ok_btn],
            actions_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )
        page.dialog = dlg

        def on_ok_click(e):
            confirm_callback()
            dlg.open = False
            page.update()

        ok_btn.on_click = on_ok_click

        def on_cancel_click(e):
            close_dlg()
            page.update()

        cancel_btn.on_click = on_cancel_click

        dlg.open = True
        page.update()

    def voltar_login(e):
        limpar_campos()
        email_input.value = ''
        page.remove(cadastro)
        page.title = 'Login Screen'
        page.appbar = ft.AppBar(title=ft.Text('Login Screen'), center_title=True)
        page.add(login)
        page.update()

    def sair_login(e):
        page.remove(alteracoes)
        page.title = 'Login Screen'
        page.appbar = ft.AppBar(title=ft.Text('Login Screen'), center_title=True)
        page.add(login)
        page.update()

    # Componentes de interface do usuário
    page.appbar = ft.AppBar(title=ft.Text('Login Screen'), center_title=True)
    nome_input = ft.TextField(
        label='Nome', autofocus=True, hint_text='Digite seu nome')
    email_input = ft.TextField(
        label='Email', autofocus=True, hint_text='Digite seu email')
    pass_input = ft.TextField(
        label='Senha', password=True, can_reveal_password=True)
    submit_btn = ft.ElevatedButton(
        text='Entrar', width=600, height=50, on_click=btn_login)
    cadastro_btn = ft.TextButton(
        text='Cadastrar', on_click=btn_cadastro)
    submeter_cadastro_btn = ft.ElevatedButton(
        text='Cadastrar', width=600, height=50, on_click=btn_submeter_cadastro)
    alterar_senha_btn = ft.TextButton(
        text='Alterar Senha', on_click=btn_alterar_senha)
    alterar_nome_btn = ft.TextButton(
        text='Alterar Nome', on_click=btn_alterar_nome)
    alterar_email_btn = ft.TextButton(
        text='Alterar Email', on_click=btn_alterar_email)
    ok_btn = ft.ElevatedButton(
        "OK")
    cancel_btn = ft.TextButton(
        text='Cancelar', on_click=close_dlg)
    voltar_btn = ft.TextButton(
        text='Voltar', on_click=voltar_login)
    sair_btn = ft.TextButton(
        text='Sair', on_click=sair_login)

    login = ft.Column([ft.Container(content=email_input,),
                       ft.Container(content=pass_input,),
                       ft.Container(content=submit_btn,),
                       ft.Container(content=cadastro_btn, alignment=ft.alignment.top_right),])

    cadastro = ft.Column([ft.Container(content=nome_input,),
                          ft.Container(content=email_input,),
                          ft.Container(content=pass_input,),
                          ft.Container(content=submeter_cadastro_btn,),
                          ft.Container(content=voltar_btn, alignment=ft.alignment.top_right),])

    alteracoes = ft.Column([ft.Container(content=sair_btn, alignment=ft.alignment.top_right,),
                            ft.Row([ft.Container(content=alterar_senha_btn,),
                                    ft.Container(content=alterar_nome_btn,),
                                    ft.Container(content=alterar_email_btn,),]),])

    page.update()
    page.add(login)


if __name__ == '__main__':
    ft.app(target=main)
