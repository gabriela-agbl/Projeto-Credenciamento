from Sistema_Credenciamento import conectar_banco
import re
import random
import time
import string
import os
from Sistema_Credenciamento.logger_utils import log_acesso

def validar_nome(nome):
    return all(c.isalpha() or c.isspace() for c in nome)

def validar_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+",email)

def validar_senha_forte(senha):
    criterios = [
        len(senha) >= 8,
        re.search(r"[A-Za-z]", senha) is not None,
        re.search(r"\d", senha) is not None,
        re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?/~]", senha) is not None
    ]
    return all(criterios)

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
    print("\n--- CADASTRO DE USUÁRIO ---")
    con = conectar_banco.conectar()
    cursor = con.cursor()
    credencial = gerar_credencial()

    while True:
        nome = input("\nDigite o nome do usuário: ")
    
        if not validar_nome(nome):
            print("Nome inválido!Use apenas letras(sem números ou símbolos).")
            log_acesso("Sistema", "Validação de nome", "Falha: Nome inválido")

        else:
            break

    while True:
        email = input("\nDigite o EMAIL do usuário: ")

        if not validar_email(email):
            print("Formato de email inválido. Ex: nome@exemplo.com")
            log_acesso(email, "Validação de email", "Falha: Formato inválido")

            continue

        cursor.execute("SELECT * FROM USUARIO WHERE email = %s", (email,))

        if cursor.fetchone():
            print("\nJá existe um usuário com esse E-mail. Tente outro!")
            log_acesso(email, "Validação de email", "Falha: Email já existe")
        
        else:
            break

    while True:
        senha = input("\nDigite a Senha (mínimo 8 caracteres, letras, números e símbolos): ").strip()

        if not validar_senha_forte(senha):
            print("\nA senha não atende aos critérios! Tente novamente.")
            log_acesso(email, "Validação de senha", "Falha - Senha fraca")
        else:
            break

    tipo = ""

    while tipo not in ["Organizador", "Participante"]:
        tipo = input("\nTipo (Organizador/Participante): ").strip().capitalize()
        if tipo not in ["Organizador", "Participante"]:
            print("\nTipo Inválido! Digite Organizador ou Participante.")
            log_acesso(email, "Validação de tipo", "Falha: Tipo inválido")
    
    if tipo == "Organizador":
        while True:
            chave_usuario = input("\nDigite a chave temporária: ").strip()

            if validar_chave(chave_usuario):
                print("\nAcesso concedido! Bem vindo!")
                print(f"Sua chave de acesso é: {credencial}")
                log_acesso(email, "Validação de chave organizador", "Sucesso")
                break
            else:
                print("\nChave inválida. Tente novamente.")
                log_acesso(email, "Validação de chave organizador", "Falha: Chave inválida")
                time.sleep(1)

    elif tipo == "Participante":
        print("\nAcesso concedido! Bem vindo!")
        print(f"Sua chave de acesso é: {credencial}")
        log_acesso(email, "Cadastro participante", "Sucesso")

    sql = "INSERT INTO USUARIO (nome, email, senha, tipo_usuario, credencial) VALUES (%s, %s, %s, %s, %s)"
    valores = (nome, email, senha, tipo, credencial)

    cursor.execute(sql, valores)
    con.commit()
    log_acesso(email, "Cadastro de Usuário", "Sucesso")

    print("\nUsuário Cadastrado com Sucesso!")

    cursor.close()
    con.close()

def atualizar_porId():
    print("\n--- ATUALIZAÇÃO DE USUÁRIO ---")
    con = conectar_banco.conectar()
    cursor = con.cursor()

    id_usuario = int(input("\nDigite o ID do usuário que deseja atualizar: "))

    select = "SELECT * FROM USUARIO WHERE id_usuario = %s"
    
    cursor.execute(select, (id_usuario,))
    resultado = cursor.fetchone()

    if resultado is None:
        
        print("\nNenhum usuário encontrado com esse ID. Tente novamente.")
        log_acesso("Sistema", f"Atualização usuário ID {id_usuario}", "Falha: Usuário não encontrado")

    else:
        email_atual = resultado[2]

        while True:
            novo_nome = input("\nDigite o novo nome: ") 
        
            if not validar_nome(novo_nome):
                print("Nome inválido!Use apenas letras(sem números ou símbolos).")
                log_acesso(email_atual, "Validação nome atualização", "Falha: Nome inválido")

            else:
                break

        while True:
            novo_email = input("\nDigite o novo email: ")
        
            if not validar_email(novo_email):
                print("Formato de email inválido. Ex: nome@exemplo.com")
                log_acesso(email_atual, "Validação email atualização", "Falha: Formato inválido")

                continue

            if novo_email == email_atual:
                break

            cursor.execute("SELECT * FROM USUARIO WHERE email = %s", (novo_email,))
            resultado_email = cursor.fetchone()

            if resultado_email and resultado_email[0] != id_usuario:
                print("\nJá existe um usuário com esse E-mail. Tente outro!")
                log_acesso(email_atual, "Validação email atualização", "Falha: Email já existe")
        
            else:
                break
        
        nova_senha = input("\nDigite a nova senha: ").strip()
        novo_tipo = input("\nDigite o novo tipo do usuário(Organizador ou Participante): ").strip().capitalize()

        sql = "UPDATE USUARIO SET nome = %s, email = %s, senha = %s, tipo_usuario = %s WHERE id_usuario = %s"
        valores = (novo_nome, novo_email, nova_senha, novo_tipo, id_usuario)

        cursor.execute(sql, valores)
        con.commit()
        log_acesso(novo_email, f"Atualização usuário ID {id_usuario}", "Sucesso")

        print("\nUsuário Atualizado com Sucesso!")

        cursor.close()
        con.close()

def deletar_porId():
    print("\n--- DELETAR USUÁRIO ---")
    con = conectar_banco.conectar()
    cursor = con.cursor()

    id_usuario = int(input("\nDigite o ID do usuário que deseja deletar: "))

    select = "SELECT * FROM USUARIO WHERE id_usuario = %s"

    cursor.execute(select, (id_usuario,))
    resultado = cursor.fetchone()

    if resultado is None:

        print("\nNenhum usuário encontrado com esse ID. Tente novamente.")
        log_acesso("Sistema", f"Exclusão usuário ID {id_usuario}", "Falha: Usuário não encontrado")

    else:
        email_usuario = resultado[2]

        sql = "DELETE FROM USUARIO WHERE id_usuario = %s"
        valores = (id_usuario,)

        cursor.execute(sql, valores)
        con.commit()
        log_acesso(email_usuario, f"Exclusão usuário ID {id_usuario}", "Sucesso")

        print("\nUsuário Deletado com Sucesso!")

def listar():

    con = conectar_banco.conectar()
    cursor = con.cursor()

    sql = "SELECT id_usuario, nome, email, tipo FROM USUARIO"
        
    cursor.execute(sql)
        
    USUARIO = cursor.fetchall()

    if USUARIO:

        print("\nUsuários Cadastrados: ")

        for usuario in USUARIO:
            print(usuario)
        log_acesso("Sistema", "Listagem de usuários", "Sucesso")

    else:
        print("\nNenhum Usuário Encontrado")
        log_acesso("Sistema", "Listagem de usuários", "Falha: Nenhum usuário encontrado")

    cursor.close()
    con.close()