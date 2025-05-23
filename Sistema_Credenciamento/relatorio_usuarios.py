from Sistema_Credenciamento import conectar_banco
from Sistema_Credenciamento.logger_utils import log_acesso

def gerar_relatorio_usuarios():
    with conectar_banco.conectar() as con, con.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM USUARIO")
        usuarios = cursor.fetchall()

    if usuarios:
        print("\n=== RELATÓRIO DE USUÁRIOS ===")
        for usuario in usuarios:
            print(
                f"ID: {usuario['id_usuario']} | "
                f"Nome: {usuario['nome']} | "
                f"Email: {usuario['email']} | "
                f"Tipo: {usuario['tipo_usuario'].capitalize()} | "
                f"Credencial: {usuario['credencial']}"
            )
        log_acesso("Sistema", "Relatório de Usuários", "Gerado com sucesso")

    else:
        print("\nNenhum usuário cadastrado.")
        log_acesso("Sistema", "Relatório de Usuários", "Nenhum dado encontrado")