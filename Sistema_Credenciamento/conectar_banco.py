import mysql.connector

def conectar():
    
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Projeto2025!",
        database="teste2"
    )
