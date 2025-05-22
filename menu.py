from Sistema_Credenciamento import User_CRUD
from Sistema_Credenciamento import login_page

def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Cadastrar Usuário")
        print("2 - Fazer Login")
        print("3 - Atualizar Usuário por ID")
        print("4 - Deletar usuário por ID")
        print("5 - Listar usuários ")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            User_CRUD.cadastrar()

        elif opcao == "2":
            login_page.login()
        
        elif opcao == "3":
            User_CRUD.atualizar_porId()
        
        elif opcao == "4":
            User_CRUD.deletar_porId()
        
        elif opcao == "5":
            User_CRUD.listar()
        
        elif opcao == "6":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida.")

menu()