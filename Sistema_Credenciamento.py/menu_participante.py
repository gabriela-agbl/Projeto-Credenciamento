import conectar_banco
import login_page

def menu_participante(id_usuario):
    while True:
        print("\n--- MENU PARTICIPANTE ---")
        print("\n1 - Ver eventos")
        print("\n2 - Inscrever-se em evento")
        print("\n3 - Sair e voltar para a tela de login")

        opcao = input("\nEscolha uma opção: ")
        # Kayque vai colocar o gerenciamento dos eventos
        if opcao == "3":
            login_page.login()