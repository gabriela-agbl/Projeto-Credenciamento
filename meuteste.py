import sqlite3

con = sqlite3.connect("teste.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS exemplo (id INTEREGER PRIMARY KEY, nome TEXT)")
con.commit()
con.close()

print("Banco criado com sucesso!")