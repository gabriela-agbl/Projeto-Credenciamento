import conectar_banco
import login_page

def menu_participante(id_usuario):
    while True:
        print("\n--- MENU PARTICIPANTE ---")
        print("1 - Ver eventos")
        print("2 - Inscrever-se em evento")
        print("3 - Sair e voltar para o menu principal")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            ver_eventos()

        elif opcao == "2":
            inscrever_em_evento(id_usuario)

        elif opcao == "3":
            from menu import menu
            menu()

        else:
            print("Opção inválida.")

def ver_eventos():
    con = conectar_banco.conectar()
    cursor = con.cursor()

    cursor.execute("SELECT id_evento, nome, data_inicio FROM EVENTO")
    eventos = cursor.fetchall()

    if eventos:
        print("\n--- Eventos Disponíveis ---")
        for evento in eventos:
            print(f"\nID: {evento[0]}")
            print(f"Nome: {evento[1]}")
            print(f"Data: {evento[2]}")
    else:
        print("\nNenhum evento cadastrado.")

    cursor.close()
    con.close()

def inscrever_em_evento(id_usuario):
    ver_eventos()
    
    id_evento = input("\nDigite o ID do evento que deseja se inscrever: ")

    con = conectar_banco.conectar()
    cursor = con.cursor()

    # Verifica se o evento existe
    cursor.execute("SELECT * FROM EVENTO WHERE id_evento = %s", (id_evento,))
    evento = cursor.fetchone()

    if not evento:
        print("\nEsse evento não existe. Tente novamente com um ID válido.")
        cursor.close()
        con.close()
        return

    # Verifica se o usuário já está inscrito nesse evento
    cursor.execute("SELECT * FROM INSCRICAO WHERE id_usuario = %s AND id_evento = %s", (id_usuario, id_evento))
    inscricao_existente = cursor.fetchone()

    if inscricao_existente:
        print("\nVocê já está inscrito nesse evento.")
    else:
        cursor.execute("INSERT INTO INSCRICAO (id_usuario, id_evento) VALUES (%s, %s)", (id_usuario, id_evento))
        con.commit()
        print("\nInscrição realizada com sucesso!")

    cursor.close()
    con.close()