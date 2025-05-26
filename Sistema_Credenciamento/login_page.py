from Sistema_Credenciamento import conectar_banco
from Sistema_Credenciamento import menu_organizador
from Sistema_Credenciamento import menu_participante
from Sistema_Credenciamento.logger_utils import log_acesso

def login():
    con = conectar_banco.conectar()
    cursor = con.cursor()

    email = input("\nDigite o seu E-mail: ")
    
    opcao = input("\nDigite '1' para continuar com o login ou '2' se esqueceu a senha ou credencial: ")

    if opcao == "2":
        cursor.execute("SELECT senha, credencial FROM USUARIO WHERE email = %s", (email,))
        resultado = cursor.fetchone()

        if resultado:
            senha, credencial = resultado
            print(f"\nRecuperação de dados para o e-mail: {email}")
            print(f"Senha: {senha}")
            print(f"Credencial: {credencial}")
            log_acesso(email, "Recuperação de dados", "Sucesso")
            
            senha = input("\nDigite a sua senha: ")
            credencial = input("\nDigite sua credencial: ")
    
            sql = "SELECT id_usuario, nome, tipo_usuario FROM USUARIO WHERE email = %s AND senha = %s AND credencial = %s"
            
            cursor.execute(sql, (email, senha, credencial))
            usuario = cursor.fetchone()

            if usuario:
                id_usuario, nome,   tipo_usuario =   usuario
        
                print(f"\nBem-vindo(a), {nome}!")

                if tipo_usuario == "organizador":
                    menu_organizador  .menu_organizador  (id_usuario)
        
                elif tipo_usuario == "participante":
                    menu_participante  .menu_participante  (id_usuario)
        
                else:
                    print("\nTipo de   usuário inválido!")
        
            else:
                print("\nE-mail não encontrado!")
                log_acesso(email, "Recuperação de dados", "Falha: E-mail não encontrado")
            
    elif opcao == "1":
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
            print("\nDados incorretos. Tente novamente.")
            log_acesso(email, "Login", "Falha")

    else:
        print("\nOpção Inválida!")
    
    cursor.close()
    con.close()
