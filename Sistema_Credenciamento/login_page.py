from Sistema_Credenciamento import conectar_banco
from Sistema_Credenciamento import menu_organizador
from Sistema_Credenciamento import menu_participante

def login():
    con = conectar_banco.conectar()
    cursor = con.cursor()

    email = input("\nDigite o seu E-mail: ")
    senha = input("\nDigite a sua senha: ")
    credencial = input("\nDigite sua credencial: ")
    
    sql = "SELECT id_usuario, nome, tipo_usuario FROM USUARIO WHERE email = %s AND senha = %s AND credencial = %s"
    cursor.execute(sql, (email, senha, credencial))
    usuario = cursor.fetchone()

    if usuario:
        id_usuario, nome, tipo_usuario = usuario
        
        print(f"\nBem-vindo(a), {nome}!")

        if tipo_usuario == "organizador":
            menu_organizador.menu_organizador(id_usuario)
        
        elif tipo_usuario == "participante":
            menu_participante.menu_participante(id_usuario)
        
        else:
            print("\nTipo de usuário inválido!")

    else:
        print("\nE-mail ou senha incorretos.Tente Novamente!")
    
    cursor.close()
    con.close()