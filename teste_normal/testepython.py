import mysql.connector

def conectar():
    
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Projetocdc2025!",
        database="teste1"
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
    
listar()
cadastrar()
atualizar_porId()
deletar_porId()