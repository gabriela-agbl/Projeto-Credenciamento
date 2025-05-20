import conectar_banco
import re
import random
import time
import string
import os

def validar_nome(nome):
    return nome.isalpha()

def validar_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+",email)

def gerar_credencial():
   return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def validar_chave(chave_inserida):
    if not os.path.exists("chave.txt"):
        print("Erro: Arquivo de chave não encontrado. Inicie o gerador primeiro.")
        return False 
    
    with open("chave.txt", "r") as arquivo:
        chave_correta = arquivo.read().strip()
        return chave_inserida.upper() == chave_correta

def cadastrar():
    
    con = conectar_banco.conectar()
    cursor = con.cursor()
    credencial = gerar_credencial()

    while True:
        nome = input("\nDigite o nome do usuário: ")
    
        if not validar_nome(nome):
            print("Nome inválido!Use apenas letras(sem números ou símbolos).")

        else:
            break

    while True:
        email = input("\nDigite o EMAIL do usuário: ")

        if not validar_email(email):
            print("Formato de email inválido. Ex: nome@exemplo.com")

            continue

        cursor.execute("SELECT * FROM USUARIO WHERE email = %s", (email,))

        if cursor.fetchone():
            print("\nJá existe um usuário com esse E-mail. Tente outro!")
        
        else:
            break

    tipo = ""

    while tipo not in ["Organizador", "Participante"]:
        tipo = input("\nTipo (Organizador/Participante): ").strip().capitalize()
        if tipo not in ["Organizador", "Participante"]:
            print("\nTipo Inválido! Digite Organizador ou Participante.")
    
    if tipo == "Organizador":
        while True:
            chave_usuario = input("\nDigite a chave temporária: ").strip()

            if validar_chave(chave_usuario):
                print("\nAcesso concedido! Bem vindo!")
                print(f"Sua chave de acesso é: {credencial}")
                break
            else:
                print("\nChave inválida. Tente novamente.")
                time.sleep(1)

    elif tipo == "Participante":
        print("\nAcesso concedido! Bem vindo!")
        print(f"Sua chave de acesso é: {credencial}")

    senha = input("\nDigite a senha do usuário: ")
    tipo_usuario = input("\nDigite o tipo de usuário(Organizador ou Participante): ")

    sql = "INSERT INTO USUARIO (nome, email, senha, tipo_usuario, credencial) VALUES (%s, %s, %s, %s, %s)"
    valores = (nome, email, senha, tipo_usuario, credencial)

    cursor.execute(sql, valores)
    con.commit()

    print("\nUsuário Cadastrado com Sucesso!")

    cursor.close()
    con.close()

def atualizar_porId():
    
    con = conectar_banco.conectar()
    cursor = con.cursor()

    id_usuario = int(input("\nDigite o ID do usuário que deseja atualizar: "))

    select = "SELECT * FROM USUARIO WHERE id_usuario = %s"
    
    cursor.execute(select, (id_usuario,))
    resultado = cursor.fetchone()

    if resultado is None:
        
        print("\nNenhum usuário encontrado com esse ID. Tente novamente.")

    else:

        while True:
            novo_nome = input("\nDigite o novo nome: ") 
        
            if not validar_nome(novo_nome):
                print("Nome inválido!Use apenas letras(sem números ou símbolos).")

            else:
                break

        while True:
            novo_email = input("\nDigite o novo email: ")
        
            if not validar_email(novo_email):
                print("Formato de email inválido. Ex: nome@exemplo.com")

                continue

            if novo_email == resultado[2]:
                break

            cursor.execute("SELECT * FROM USUARIO WHERE email = %s", (novo_email,))

            if cursor.fetchone():
                print("\nJá existe um usuário com esse E-mail. Tente outro!")
        
            else:
                break
        
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

    con = conectar_banco.conectar()
    cursor = con.cursor()

    id_usuario = int(input("\nDigite o ID do usuário que deseja deletar: "))

    select = "SELECT * FROM USUARIO WHERE id_usuario = %s"

    cursor.execute(select, (id_usuario,))
    resultado = cursor.fetchone()

    if resultado is None:

        print("\nNenhum usuário encontrado com esse ID. Tente novamente.")

    else:

        sql = "DELETE FROM USUARIO WHERE id_usuario = %s"
        valores = (id_usuario,)

        cursor.execute(sql, valores)
        con.commit()

        print("\nUsuário Deletado com Sucesso!")

def listar():

    con = conectar_banco.conectar()
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