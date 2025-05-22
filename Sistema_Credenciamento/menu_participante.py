from Sistema_Credenciamento import conectar_banco
from Sistema_Credenciamento.logger_utils import log_acesso

def menu_participante(id_usuario):
    while True:
        print("\n--- MENU PARTICIPANTE ---")
        print("1 - Ver eventos")
        print("2 - Inscrever-se em evento")
        print("3 - Sair e voltar para o menu principal")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            ver_eventos(id_usuario)

        elif opcao == "2":
            inscrever_em_evento(id_usuario)

        elif opcao == "3":
            print("Voltando ao menu principal...")
            return

        else:
            print("Opção inválida.")

def ver_eventos(id_usuario):
    con = conectar_banco.conectar()
    cursor = con.cursor()

    cursor.execute("SELECT email FROM USUARIO WHERE id_usuario = %s", (id_usuario,))
    email = cursor.fetchone()[0]

    cursor.execute("SELECT id_evento, nome, data_inicio FROM EVENTO")
    eventos = cursor.fetchall()

    if eventos:
        print("\n--- Eventos Disponíveis ---")
        for evento in eventos:
            print(f"\nID: {evento[0]}")
            print(f"Nome: {evento[1]}")
            print(f"Data: {evento[2]}")
        log_acesso(email, "Visualização de Eventos", "Sucesso")
    else:
        print("\nNenhum evento cadastrado.")
        log_acesso(email, "Visualização de Eventos", "Nenhum evento encontrado")

    cursor.close()
    con.close()

def inscrever_em_evento(id_usuario):
    con = conectar_banco.conectar()
    cursor = con.cursor()

    cursor.execute("SELECT email FROM USUARIO WHERE id_usuario = %s", (id_usuario,))
    email = cursor.fetchone()[0]

    ver_eventos(id_usuario)
    
    id_evento = input("\nDigite o ID do evento que deseja se inscrever: ")

    # Verifica se o evento existe
    cursor.execute("SELECT * FROM EVENTO WHERE id_evento = %s", (id_evento,))
    evento = cursor.fetchone()

    if not evento:
        print("\nEsse evento não existe. Tente novamente com um ID válido.")
        log_acesso(email, "Inscrição em Evento", "Falha: Evento não encontrado")
        cursor.close()
        con.close()
        return

    # Verifica se o usuário já está inscrito nesse evento
    cursor.execute("SELECT * FROM INSCRICAO WHERE id_usuario = %s AND id_evento = %s", (id_usuario, id_evento))
    inscricao_existente = cursor.fetchone()

    if inscricao_existente:
        print("\nVocê já está inscrito nesse evento.")
        log_acesso(email, "Inscrição em Evento", "Falha: Inscrição duplicada")
    else:
        cursor.execute("INSERT INTO INSCRICAO (id_usuario, id_evento) VALUES (%s, %s)", (id_usuario, id_evento))
        con.commit()
        log_acesso(email, "Inscrição em Evento", f"Sucesso: Evento {id_evento}")
        print("\nInscrição realizada com sucesso!")

    cursor.close()
    con.close()