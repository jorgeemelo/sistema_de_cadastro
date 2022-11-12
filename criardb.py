# importando o SQLite
import sqlite3 as lite

# criando conexão
con = lite.connect('dados.db')

'''
# criando tabela (old)
with con:
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE Inventario(id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT, local TEXT, descricao TEXT,marca TEXT,  data_da_compra DATE, valor_da_compra DECIMAL, serie TEXT)"
        )
'''

# Criando tabela Cadastro
with con:
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE Cadastro(id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT, data_de_nasc DATE, nome_pai TEXT, nome_mae TEXT, casados TEXT, padrinho TEXT, madrinha TEXT)"
        )

############## Celulas do Cadastro ##############
# nome
# data de nasc
# nome pai
# nome mae
# casados na igreja () sim () nao
# padrinho
# madrinha
# celebrante
# dia do batismo
