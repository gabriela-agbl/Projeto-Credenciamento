import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Projetocdc2025!",
    database="teste1"
)

cursor = con.cursor()

nome = "Joao Silva"
email = "joao@gmail.com"
senha = 123456
tipo_usuario = "participante"

sql = "INSERT INTO USUARIO (nome, email, senha, tipo_usuario) VALUES (%s, %s, %s, %s)"
valores = (nome, email, senha, tipo_usuario)

cursor.execute(sql, valores)
con.commit()

print("usuario cadastrado com sucesso")

cursor.close()
con.close()