import mysql.connector
import User_CRUD

def criar_banco():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Projetocdc2025!",
        database="teste2"
    )
    cursor = con.cursor()

    with open("teste_com_menu/teste2.sql", "r") as arquivo:
        comandos = arquivo.read().split(';')
        for comando in comandos:
            if comando.strip() != "":
                cursor.execute(comando)
    con.commit()
    cursor.close()
    con.close()

def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Cadastrar Usuário")
        print("2 - Atualizar Usuário por ID")
        print("3 - Deletar usuário por ID")
        print("4 - Listar usuários ")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            User_CRUD.cadastrar()
        
        elif opcao == "2":
            User_CRUD.atualizar_porId()
        
        elif opcao == "3":
            User_CRUD.deletar_porId()
        
        elif opcao == "4":
            User_CRUD.listar()
        
        elif opcao == "5":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida.")

criar_banco()
menu()