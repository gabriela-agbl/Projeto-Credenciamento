import conectar_banco
import login_page

def menu_organizador(id_usuario):
    while True:
        print("\n--- MENU ORGANIZADOR ---")
        print("\n1 - Criar evento")
        print("\n2 - Ver participantes dos eventos")
        print("\n3 - Sair e voltar para a tela de login")

        opcao = input("\nEscolha uma opção: ")
        # Kayque vai colocar o gerenciamento dos eventos
        if opcao == "3":
            login_page.login()