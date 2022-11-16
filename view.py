import sqlite3 as lite
from datetime import datetime

# Criando conexão
con = lite.connect('dados.db')

# Inserir Cadastros
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Cadastro (nome, data_de_nasc, nome_pai, nome_mae, casados, padrinho, madrinha, celebrante, dia_batismo) VALUES (?,?,?,?,?,?,?,?,?)"
        cur.execute(query, i)


# Deletar Cadastros
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Cadastro WHERE id=?"
        cur.execute(query, i)


# Atualizar Cadastros
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Cadastro SET nome=?, data_de_nasc=?, nome_pai=?, nome_mae=?, casados=?, padrinho=?, madrinha=?, celebrante=?, dia_batismo=?"
        cur.execute(query, i)


# Ver Cadastro
def ver_form():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Cadastro")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens


# Ver Item no Cadastros
def ver_iten(id):
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Cadastro WHERE id=?",(id))
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens
