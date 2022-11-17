# add sistema de leitura de acentos (uft8) #

from tkinter import*
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkcalendar import*
import sys
from view import*

sys.setrecursionlimit(10000) # Configuracao do limite de recursao para 10000

################# cores ###############

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
co10 = "#eb4b4b" # + cancelar
co11 = "#609960" # + confirmar

################# criando janela ###############

janela = Tk ()
janela.title ("Sistema de Cadastro para Batismo")

janela.geometry('950x765')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

################# Frames ####################

frameCima = Frame(janela, width=950, height=100, bg=co1, pady=0, padx=50,  relief="flat")
frameCima.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

frameMeio = Frame(janela, width=950, height=305,bg=co1, pady=20, padx=10, relief="flat")
frameMeio.grid(row=1, column=0,pady=1, padx=0, sticky=NSEW)

frameBotoes = Frame(janela, width=950, height=80, pady=0, padx=95, bg=co1, relief="flat")
frameBotoes.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

frameBottom = Frame(janela,width=950, height=280,bg=co1, relief="flat")
frameBottom.grid(row=3, column=0, pady=0, padx=1, sticky=NSEW)

################## Cabecalho do programa #####################

app_img = Image.open('main_files\icon\icon_logo.png') # OBS: alterar logo do programa
app_img = app_img.resize((80, 80))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=" Cadastro Batismo", width=900, compound=LEFT, relief="flat", anchor=NW, font=('Verdana 20 bold'),bg=co1, fg=co4)
app_logo.place(x=220, y=8)

global tree, values

####################### FUNCOES #######################

# funcao inserir
def inserir():

    global tree, values

    nome = e_nome.get()
    data_de_nasc = e_nasc.get()
    nome_pai = e_nome_pai.get()
    nome_mae = e_nome_mae.get()
    casados = e_casados.get()
    padrinho = e_padrinho.get()
    madrinha = e_madrinha.get()
    celebrante = e_celebrante.get()
    dia_batismo = e_dia_batismo.get()

    lista_inserir = [nome, data_de_nasc, nome_pai, nome_mae, casados, padrinho, madrinha, celebrante, dia_batismo]

    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')

            return

    inserir_form(lista_inserir)

    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

    e_nome.delete(0, 'end')
    e_nasc.delete(0, 'end')
    e_nome_pai.delete(0, 'end')
    e_nome_mae.delete(0, 'end')
    e_padrinho.delete(0, 'end')
    e_madrinha.delete(0, 'end')
    e_celebrante.delete(0, 'end')
    e_dia_batismo.delete(0, 'end')

    for widget in frameBottom.winfo_children():
        widget.destroy()

    mostrar()

# funcao atualizar
def atualizar():
    
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]

        e_nome.delete(0, 'end')
        e_nasc.delete(0, 'end')
        e_nome_pai.delete(0, 'end')
        e_nome_mae.delete(0, 'end')
        #e_casados.delete(0, 'end')
        e_padrinho.delete(0, 'end')
        e_madrinha.delete(0, 'end')
        e_celebrante.delete(0, 'end')
        e_dia_batismo.delete(0, 'end')

        id = int(treev_lista[0])
        e_nome.insert(0, treev_lista[1])
        e_nasc.insert(0, treev_lista[2])
        e_nome_pai.insert(0, treev_lista[3])
        e_nome_mae.insert(0, treev_lista[4])
        #e_casados.select(0, treev_lista[5])
        e_padrinho.insert(0, treev_lista[6])
        e_madrinha.insert(0, treev_lista[7])
        e_celebrante.insert(0, treev_lista[8])
        e_dia_batismo.insert(0, treev_lista[9])

        def update():

            nome = e_nome.get()
            data_de_nasc = e_nasc.get()
            nome_pai = e_nome_pai.get()
            nome_mae = e_nome_mae.get()
            casados = e_casados.get()
            padrinho = e_padrinho.get()
            madrinha = e_madrinha.get()
            celebrante = e_celebrante.get()
            dia_batismo = e_dia_batismo.get()

            lista_atualizar = [nome, data_de_nasc, nome_pai, nome_mae, casados, padrinho, madrinha, celebrante, dia_batismo, id]

            for i in lista_atualizar:
                if i=='':
                    messagebox.showerror('Erro', 'Preencha todos os campos')

                    return

            atualizar_form(lista_atualizar)

            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

            e_nome.delete(0, 'end')
            e_nasc.delete(0, 'end')
            e_nome_pai.delete(0, 'end')
            e_nome_mae.delete(0, 'end')
            #e_casados.delete(0, 'end')
            e_padrinho.delete(0, 'end')
            e_madrinha.delete(0, 'end')
            e_celebrante.delete(0, 'end')
            e_dia_batismo.delete(0, 'end')
            #
            # RECRIAR BOTÃO E LABEL PARA OCULTAR DEL E REG
            #
            botao_confirmar.destroy()
            botao_cancelar.destroy()
            
            for widget in frameBottom.winfo_children():
                widget.destroy()

            mostrar()
        
        def cancelar():
            
            e_nome.delete(0, 'end')
            e_nasc.delete(0, 'end')
            e_nome_pai.delete(0, 'end')
            e_nome_mae.delete(0, 'end')
            e_padrinho.delete(0, 'end')
            e_madrinha.delete(0, 'end')
            e_celebrante.delete(0, 'end')
            e_dia_batismo.delete(0, 'end')
            
            messagebox.showinfo('Cancelado com sucesso', 'Edição cancelada. Os dados de cadastro não foram alterados.')
            
            botao_confirmar.destroy()
            botao_cancelar.destroy()        
        #
        # OBS: RECRIAR BOTÃO E LABEL PARA OCULTAR DEL E REG
        #    
        botao_confirmar = Button(frameBotoes, image=img_done, compound=LEFT, anchor=NW, text="   Salvar".upper(), width=150, overrelief=RIDGE,  font=('ivy 10 bold'),bg=co11, fg=co1, command=update)
        botao_confirmar.place(x=20, y=11)
        
        botao_cancelar = Button(frameBotoes, image=img_cancel, compound=LEFT, anchor=NW, text="   Cancelar".upper(), width=150, overrelief=RIDGE,  font=('ivy 10 bold'),bg=co10, fg=co1, command=cancelar)
        botao_cancelar.place(x=380, y=11) # OBS: COLOCAR NO LUGAR DO BOTÃO EDITAR #

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')

# funcao deletar
def deletar():

    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]

        deletar_form([valor])

        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

        for widget in frameBottom.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')

####################### VARIAVEIS DE ENTRADA #######################

l_nome = Label(frameMeio, text="Nome", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=20, y=10)
e_nome = Entry(frameMeio, width=40, justify='left',relief="solid")
e_nome.place(x=150, y=11)

l_nasc = Label(frameMeio, text="Data de Nascimento", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nasc.place(x=20, y=40)
e_nasc = DateEntry(frameMeio, width=12, background='darkblue', foreground='white', borderwidth=2, year=2022)
e_nasc.place(x=160, y=41)

l_nome_pai = Label(frameMeio, text="Pai", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome_pai.place(x=20, y=70)
e_nome_pai = Entry(frameMeio, width=40, justify='left',relief="solid")
e_nome_pai.place(x=150, y=71)

l_nome_mae = Label(frameMeio, text="Mãe", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome_mae.place(x=20, y=100)
e_nome_mae = Entry(frameMeio, width=40, justify='left',relief="solid")
e_nome_mae.place(x=150, y=101)

l_casados = Label(frameMeio, text="Casados na Igreja", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_casados.place(x=20, y=130)
e_casados = StringVar('')
cb_casados = ttk.Combobox(frameMeio, width=10, textvariable=e_casados)
cb_casados['values'] = ['Sim', 'Não']
cb_casados['state'] = 'readonly'
cb_casados.bind('<<ComboboxSelected>>', e_casados.get())
cb_casados.place(x=150, y=131)

l_padrinho = Label(frameMeio, text="Padrinho", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_padrinho.place(x=20, y=160)
e_padrinho = Entry(frameMeio, width=40, justify='left',relief="solid")
e_padrinho.place(x=150, y=161)

l_madrinha = Label(frameMeio, text="Madrinha", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_madrinha.place(x=20, y=190)
e_madrinha = Entry(frameMeio, width=40, justify='left',relief="solid")
e_madrinha.place(x=150, y=191)

l_celebrante = Label(frameMeio, text="Celebrante", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_celebrante.place(x=20, y=220)
e_celebrante = Entry(frameMeio, width=40, justify='left',relief="solid")
e_celebrante.place(x=150, y=221)

l_dia_batismo = Label(frameMeio, text="Dia do Batismo", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_dia_batismo.place(x=20, y=250)
e_dia_batismo = DateEntry(frameMeio, width=12, background='darkblue', foreground='white', borderwidth=2, year=2022)
e_dia_batismo.place(x=150, y=251)

# Botao Inserir
img_add = Image.open('main_files\icon\icon_add.png')
img_add = img_add.resize((50, 50))
img_add = ImageTk.PhotoImage(img_add)

botao_inserir = Button(frameBotoes, image=img_add, compound=LEFT, anchor=NW, text="   Cadastrar".upper(), width=150, overrelief=RIDGE,  font=('ivy 10'),bg=co1, fg=co0, command=inserir)
botao_inserir.place(x=20, y=11)

# Botao Atualizar/Editar
img_done = Image.open('main_files\icon\icon_done.png')
img_done = img_done.resize((50, 50))
img_done = ImageTk.PhotoImage(img_done)

img_cancel = Image.open('main_files\icon\icon_cancel.png')
img_cancel = img_cancel.resize((50, 50))
img_cancel = ImageTk.PhotoImage(img_cancel)

img_update = Image.open('main_files\icon\icon_edit.png')
img_update = img_update.resize((50, 50))
img_update = ImageTk.PhotoImage(img_update)

botao_atualizar = Button(frameBotoes, image=img_update, compound=LEFT, anchor=NW, text="   Editar".upper(), width=150, overrelief=RIDGE,  font=('ivy 10'),bg=co1, fg=co0, command=atualizar)
botao_atualizar.place(x=200, y=11)

# Botao Deletar
img_delete  = Image.open('main_files\icon\icon_delete.png')
img_delete = img_delete.resize((50, 50))
img_delete = ImageTk.PhotoImage(img_delete)

botao_deletar = Button(frameBotoes, image=img_delete, compound=LEFT, anchor=NW, text="   Excluir".upper(), width=150, overrelief=RIDGE,  font=('ivy 10'),bg=co1, fg=co0, command=deletar)
botao_deletar.place(x=380, y=11)

# Botao ver Item
img_item  = Image.open('main_files\icon\icon_item.png')
img_item = img_item.resize((50, 50))
img_item = ImageTk.PhotoImage(img_item)

botao_ver = Button(frameBotoes, image=img_item, compound=LEFT, anchor=NW, text="   NULL".upper(), width=150, overrelief=RIDGE,  font=('ivy 10'),bg=co1, fg=co0)
botao_ver.place(x=560, y=11)

####################### TELA DE PRINT DOS REGISTROS DO DB #######################

# funcao para criar treeview com os dados de cadastro
def mostrar():
    # creating a treeview with dual scrollbars
    tabela_head = ['#ID','Nome', 'Data de Nascimento', 'Nome do Pai', 'Nome da Mãe', 'Casados na Igreja', 'Padrinho', 'Madrinha', 'Celebrante', 'Dia do Batismo']

    global tree, values, id

    tree = ttk.Treeview(frameBottom, selectmode="extended",columns=tabela_head, show="headings")
    
    # vertical scrollbar
    vsb = ttk.Scrollbar(frameBottom, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameBottom, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBottom.grid_rowconfigure(0, weight=12)

    h=[30,100,100,100,100,100,100,100,100,100]
    mh=[30,100,100,100,100,100,100,100,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)

        # adjust the column's width to the header string
        tree.column(col, width=h[n],minwidth=mh[n],anchor=CENTER)
        n+=1
    
    lista_itens = []
    
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Cadastro")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)

    count = 0
    for items in lista_itens:
        tree.insert(parent='', index='end', iid = count, values=(items[0], items[1], items[2], items[3], items[4], items[5], items[6], items[7], items[8], items[9]))
        count += 1

mostrar()

janela.mainloop()