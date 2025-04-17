import conectar_banco
import menu_organizador
import menu_participante

def login():
    con = conectar_banco.conectar()
    cursor = con.cursor()

    email = input("\nDigite o seu E-mail: ")
    senha = input("\nDigite a sua senha: ")
    
    sql = "SELECT id_usuario, nome, tipo_usuario FROM USUARIO WHERE email = %s AND senha = %s"
    cursor.execute(sql, (email, senha))
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