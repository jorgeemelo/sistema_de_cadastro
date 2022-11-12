# importando o SQLite
import sqlite3 as lite

# criando conexão
con = lite.connect('dados.db')

# criando tabela
with con:
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE Inventario(id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT, local TEXT, descricao TEXT,marca TEXT,  data_da_compra DATE, valor_da_compra DECIMAL, serie TEXT)"
        )
