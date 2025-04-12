import mysql.connector

def conectar():
    
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Projetocdc2025!",
        database="teste2"
    )
