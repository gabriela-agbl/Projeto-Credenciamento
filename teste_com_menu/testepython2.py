import mysql.connector

def conectar():
    
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Projetocdc2025!",
        database="teste2"
    )

def cadastrar():
    
    con = conectar()
    cursor = con.cursor()

    nome = input("\nDigite o nome do usuário: ")
    email = input("\nDigite o EMAIL do usuário: ")
    senha = input("\nDigite a senha do usuário: ")
    tipo_usuario = input("\nDigite o tipo de usuário(Organizador ou Participante): ")

    sql = "INSERT INTO USUARIO (nome, email, senha, tipo_usuario) VALUES (%s, %s, %s, %s)"
    valores = (nome, email, senha, tipo_usuario)

    cursor.execute(sql, valores)
    con.commit()

    print("\nUsuário Cadastrado com Sucesso!")

    cursor.close()
    con.close()

def atualizar_porId():
    
    con = conectar()
    cursor = con.cursor()

    id_usuario = int(input("\nDigite o ID do usuário que deseja atualizar: "))
    novo_nome = input("\nDigite o novo nome: ") 
    novo_email = input("\nDigite o novo email: ")
    nova_senha = input("\nDigite a nova senha: ")
    novo_tipo = input("\nDigite o novo tipo do usuário(Organizador ou Participante): ")

    sql = "UPDATE USUARIO SET nome = %s, email = %s, senha = %s, tipo_usuario = %s WHERE id_usuario = %s"
    valores = (novo_nome, novo_email, nova_senha, novo_tipo, id_usuario)

    cursor.execute(sql, valores)
    con.commit()

    print("\nUsuário Atualizado com Sucesso!")

    cursor.close()
    con.close()

def deletar_porId():

    con = conectar()
    cursor = con.cursor()

    id_usuario = int(input("\nDigite o ID do usuário que deseja deletar: "))

    sql = "DELETE FROM USUARIO WHERE id_usuario = %s"
    valores = (id_usuario,)

    cursor.execute(sql, valores)
    con.commit()

    print("\nUsuário Deletado com Sucesso!")

def listar():

    con = conectar()
    cursor = con.cursor()

    sql = "SELECT * FROM USUARIO"
        
    cursor.execute(sql)
        
    USUARIO = cursor.fetchall()

    if USUARIO:

        print("\nUsuários Cadastrados: ")

        for usuario in USUARIO:
            print(usuario)

    else:
        print("\nNenhum Usuário Encontrado")

    cursor.close()
    con.close()
def criar_banco():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Projetocdc2025!",
        database="teste2"
    )
    cursor = con.cursor()

    with open("teste2.sql", "r") as arquivo:
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
            cadastrar()
        elif opcao == "2":
            atualizar_porId()
        elif opcao == "3":
            deletar_porId()
        elif opcao == "4":
            listar()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

criar_banco()
menu()