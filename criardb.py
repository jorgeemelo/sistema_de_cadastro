# importando o SQLite
import sqlite3 as lite

# criando conexão
con = lite.connect('dados.db')

# Criando tabela Cadastro
with con:
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE Cadastro(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, data_de_nasc DATE, nome_pai TEXT, nome_mae TEXT, casados TEXT, padrinho TEXT, madrinha TEXT, celebrante TEXT, dia_batismo DATE)"
        )