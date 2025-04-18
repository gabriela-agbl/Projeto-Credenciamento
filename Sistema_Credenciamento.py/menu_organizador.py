import re
import conectar_banco
import login_page

def menu_organizador(id_usuario):
    while True:
        print("\n--- MENU ORGANIZADOR ---")
        print("1 - Criar evento")
        print("2 - Ver participantes dos eventos")
        print("3 - Apagar evento")
        print("4 - Sair e voltar para o menu principal")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            criar_evento(id_usuario)

        elif opcao == "2":
            ver_participantes(id_usuario)

        elif opcao == "3":
            apagar_evento(id_usuario)

        elif opcao == "4":
            from menu import menu
            menu()

        else:
            print("Opção inválida.")

def validar_data(data):
    # Expressão regular para o formato AAAA-MM-DD
    return re.fullmatch(r"\d{4}-\d{2}-\d{2}", data)

def criar_evento(id_organizador):
    con = conectar_banco.conectar()
    cursor = con.cursor()

    nome = input("\nDigite o nome do evento: ")

    while True:
        data_inicio = input("Digite a data inicial do evento (formato AAAA-MM-DD): ")
        if validar_data(data_inicio):
            break
        print("Data inválida. Digite no formato correto (AAAA-MM-DD), apenas números e traços.")

    while True:
        data_fim = input("Digite a data final do evento (formato AAAA-MM-DD): ")
        if validar_data(data_fim):
            break
        print("Data inválida. Digite no formato correto (AAAA-MM-DD), apenas números e traços.")

    sql = """
        INSERT INTO EVENTO (
            nome, data_inicio, data_fim, id_organizador
        ) VALUES (%s, %s, %s, %s)
    """
    valores = (nome, data_inicio, data_fim, id_organizador)

    cursor.execute(sql, valores)
    con.commit()

    print("\nEvento criado com sucesso!")

    cursor.close()
    con.close()

def ver_participantes(id_organizador):
    con = conectar_banco.conectar()
    cursor = con.cursor()

    cursor.execute("SELECT id_evento, nome FROM EVENTO WHERE id_organizador = %s", (id_organizador,))
    eventos = cursor.fetchall()

    if not eventos:
        print("\nVocê ainda não criou nenhum evento.")
        cursor.close()
        con.close()
        return

    print("\n--- Seus Eventos ---")
    for evento in eventos:
        print(f"{evento[0]} - {evento[1]}")

    id_evento = input("\nDigite o ID do evento que deseja ver os participantes: ")

    sql = """
    SELECT U.nome, U.email
    FROM INSCRICAO I
    JOIN USUARIO U ON I.id_usuario = U.id_usuario
    WHERE I.id_evento = %s
    """
    cursor.execute(sql, (id_evento,))
    participantes = cursor.fetchall()

    if participantes:
        print("\n--- Participantes Inscritos ---")
        for p in participantes:
            print(f"Nome: {p[0]}, Email: {p[1]}")
    else:
        print("\nNenhum participante inscrito nesse evento.")

    cursor.close()
    con.close()

def apagar_evento(id_organizador):
    con = conectar_banco.conectar()
    cursor = con.cursor()

    cursor.execute("SELECT id_evento, nome FROM EVENTO WHERE id_organizador = %s", (id_organizador,))
    eventos = cursor.fetchall()

    if not eventos:
        print("\nVocê não tem eventos para apagar.")
        cursor.close()
        con.close()
        return

    print("\n--- Seus Eventos ---")
    for evento in eventos:
        print(f"{evento[0]} - {evento[1]}")

    id_evento = input("\nDigite o ID do evento que deseja apagar: ")

    # Verifica se o evento pertence ao organizador
    evento_ids = [str(e[0]) for e in eventos]
    if id_evento not in evento_ids:
        print("Evento não encontrado ou você não tem permissão para apagá-lo.")
        cursor.close()
        con.close()
        return

    # Confirmação
    confirmacao = input("Tem certeza que deseja apagar este evento? Isso removerá também todas as inscrições. (s/n): ").lower()
    if confirmacao != "s":
        print("Operação cancelada.")
        cursor.close()
        con.close()
        return

    # Remove inscrições relacionadas
    cursor.execute("DELETE FROM INSCRICAO WHERE id_evento = %s", (id_evento,))

    # Remove o evento
    cursor.execute("DELETE FROM EVENTO WHERE id_evento = %s AND id_organizador = %s", (id_evento, id_organizador))
    con.commit()

    print("\nEvento apagado com sucesso.")

    cursor.close()
    con.close()
