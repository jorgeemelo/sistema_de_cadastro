from tkinter import*
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkcalendar import*

from view import atualizar_form, deletar_form, inserir_form, ver_form

################# cores ###############
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # padrinho
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

################# criando janela ###############

janela = Tk ()
janela.title ("Sistema de Cadastro para Batismo")

janela.geometry('900x715')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

################# Frames ####################

frameCima = Frame(janela, width=1028, height=50, bg=co1, pady=0, padx=50,  relief="flat")
frameCima.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

frameMeio = Frame(janela, width=1028, height=285,bg=co1, pady=20, padx=10, relief="flat")
frameMeio.grid(row=1, column=0,pady=1, padx=0, sticky=NSEW)

frameBotoes = Frame(janela, width=1028, height=80, pady=0, padx=70, bg=co1, relief="flat")
frameBotoes.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

frameDireita = Frame(janela,width=1043, height=300,bg=co1, relief="flat")
frameDireita.grid(row=3, column=0, pady=0, padx=1, sticky=NSEW)

# Cabecalho do programa
app_img = Image.open('main_files\icon\icon_logo.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=" Cadastro Batismo", width=900, compound=LEFT, relief="flat", anchor=NW, font=('Verdana 20 bold'),bg=co1, fg=co4)
app_logo.place(x=0, y=0)

global tree

# funcao inserir
def inserir():

    global imagem

    nome = e_nome.get()
    data_de_nasc = e_cal.get()
    nome_pai = e_nome_pai.get()
    nome_mae = e_nome_mae.get()
    casados = e_casados.get()
    padrinho = e_padrinho.get()
    madrinha = e_madrinha.get()

    lista_inserir = [nome, data_de_nasc, nome_pai, nome_mae, casados, padrinho, madrinha]

    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')

            return

    inserir_form(lista_inserir)

    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

    e_nome.delete(0, 'end')
    e_cal.delete(0, 'end')
    e_nome_pai.delete(0, 'end')
    e_nome_mae.delete(0, 'end')
    #e_casados.delete(0, 'end') TESTING
    e_padrinho.delete(0, 'end')
    e_madrinha.delete(0, 'end')

    for widget in frameDireita.winfo_children():
        widget.destroy()

    mostrar()

# funcao atualizar
def atualizar():

    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        padrinho = treev_lista[0]

        e_nome.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_nome_pai.delete(0, 'end')
        e_nome_mae.delete(0, 'end')
        e_casados.delete(0, 'end')
        e_padrinho.delete(0, 'end')
        e_madrinha.delete(0, 'end')

        id = int(treev_lista[0])
        e_nome.insert(0, treev_lista[1])
        e_cal.insert(0, treev_lista[2])
        e_nome_pai.insert(0, treev_lista[3])
        e_nome_mae.insert(0, treev_lista[4])
        e_casados.insert(0, treev_lista[5])
        e_padrinho.insert(0, treev_lista[6])
        e_madrinha.insert(0, treev_lista[7])


        def update():

            global imagem

            nome = e_nome.get()
            data_de_nasc = e_cal.get()
            nome_pai = e_nome_pai.get()
            nome_mae = e_nome_mae.get()
            casados = e_casados.get()
            padrinho = e_padrinho.get()
            madrinha = e_madrinha.get()

            if imagem == '':
                imagem = e_madrinha.insert(0, treev_lista[7])

            lista_atualizar = [nome, nome_pai, nome_mae, casados, data_de_nasc, padrinho, madrinha, id]

            for i in lista_atualizar:
                if i=='':
                    messagebox.showerror('Erro', 'Preencha todos os campos')

                    return

            atualizar_form(lista_atualizar)

            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

            e_nome.delete(0, 'end')
            e_cal.delete(0, 'end')
            e_nome_pai.delete(0, 'end')
            e_nome_mae.delete(0, 'end')
            e_casados.delete(0, 'end')
            e_padrinho.delete(0, 'end')
            e_madrinha.delete(0, 'end')

            botao_confirmar.destroy()

            for widget in frameDireita.winfo_children():
                widget.destroy()

            mostrar()

        botao_confirmar = Button(frameMeio, command=update, text="Confirmar".upper(), width=13, height=1, bg=co2, fg=co1,font=('ivy 8 bold'),relief=RAISED, overrelief=RIDGE)

        botao_confirmar.place(x=330, y=185)


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

        for widget in frameDireita.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')

# criando entradas
l_nome = Label(frameMeio, text="Nome", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=20, y=10)

e_nome = Entry(frameMeio, width=30, justify='left',relief="solid")
e_nome.place(x=130, y=11)

# ADICIONAR OUTRA VARIAVEL DE DATA PARA 'DIA_BATISMO'
l_cal = Label(frameMeio, text="Data de Nascimento", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cal.place(x=20, y=130)

e_cal = DateEntry(frameMeio, width=12, background='darkblue', foreground='white', borderwidth=2, year=2022)
e_cal.place(x=130, y=131)

l_nome_pai = Label(frameMeio, text="Nome do Pai", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome_pai.place(x=20, y=40)

e_nome_pai = Entry(frameMeio, width=30, justify='left',relief="solid")
e_nome_pai.place(x=130, y=41)

l_nome_mae = Label(frameMeio, text="Nome da Mãe", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome_mae.place(x=20, y=70)
e_nome_mae = Entry(frameMeio, width=30, justify='left',relief="solid")
e_nome_mae.place(x=130, y=71)



#v_casados = StringVar()
# v_casados = ttk.Combobox(janela, textvariable=d_casados)
# e_casados['values'] = ['Sim', 'Não']
# e_casados['state'] = 'readonly'
# v_casados.place(x=130, y=101)
#e_casados.bind('<<ComboboxSelected>>', v_casados.get())



l_casados = Label(frameMeio, text="Casados na Igreja", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_casados.place(x=20, y=100)

e_casados = StringVar('')
cb_casados = ttk.Combobox(frameMeio, width=10, textvariable=e_casados)
cb_casados['values'] = ['Sim', 'Não']
cb_casados.bind('<<ComboboxSelected>>', e_casados.get())
cb_casados['state'] = 'readonly'
cb_casados.place(x=130, y=101)



l_padrinho = Label(frameMeio, text="Nome do Padrinho", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_padrinho.place(x=20, y=160)

e_padrinho = Entry(frameMeio, width=30, justify='left',relief="solid")
e_padrinho.place(x=130, y=161)

l_madrinha = Label(frameMeio, text="Nome da Madrinha", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_madrinha.place(x=20, y=190)

e_madrinha = Entry(frameMeio, width=30, justify='left',relief="solid")
e_madrinha.place(x=130, y=191)

l_carregar = Label(frameMeio, text="TEXTO", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_carregar.place(x=20, y=220)

# Botao Carregar
botao_carregar = Button(frameMeio, compound=CENTER, anchor=CENTER, text="carregar".upper(), width=30, overrelief=RIDGE,  font=('ivy 8'),bg=co1, fg=co0 )
botao_carregar.place(x=130, y=221)

# Botao Inserir
img_add = Image.open('main_files\icon\icon_add.png')
img_add = img_add.resize((50, 50))
img_add = ImageTk.PhotoImage(img_add)

botao_inserir = Button(frameBotoes, image=img_add, compound=LEFT, anchor=NW, text="   Adicionar".upper(), width=150, overrelief=RIDGE,  font=('ivy 10'),bg=co1, fg=co0, command=inserir)
botao_inserir.place(x=20, y=11)

# Botao Atualizar
img_update = Image.open('main_files\icon\icon_update.png')
img_update = img_update.resize((50, 50))
img_update = ImageTk.PhotoImage(img_update)

botao_atualizar = Button(frameBotoes, image=img_update, compound=LEFT, anchor=NW, text="   Atualizar".upper(), width=150, overrelief=RIDGE,  font=('ivy 10'),bg=co1, fg=co0, command=atualizar)
botao_atualizar.place(x=200, y=11)

# Botao Deletar
img_delete  = Image.open('main_files\icon\icon_delete.png')
img_delete = img_delete.resize((50, 50))
img_delete = ImageTk.PhotoImage(img_delete)

botao_deletar = Button(frameBotoes, image=img_delete, compound=LEFT, anchor=NW, text="   Deletar".upper(), width=150, overrelief=RIDGE,  font=('ivy 10'),bg=co1, fg=co0, command=deletar)
botao_deletar.place(x=380, y=11)

# Botao ver Item
img_item  = Image.open('main_files\icon\icon_item.png')
img_item = img_item.resize((50, 50))
img_item = ImageTk.PhotoImage(img_item)

botao_ver = Button(frameBotoes, image=img_item, compound=LEFT, anchor=NW, text="   Ver item".upper(), width=150, overrelief=RIDGE,  font=('ivy 10'),bg=co1, fg=co0)
botao_ver.place(x=560, y=11)

'''
# Labels Quantidade total e padrinhoes
l_total = Label(frameMeio, width=14, height=2,anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1, relief=FLAT)
l_total.place(x=450, y=17)

l_padrinho_total = Label(frameMeio, text='  padrinho Total de todos os itens  ' ,anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_padrinho_total.place(x=450, y=12)

l_qtd = Label(frameMeio, width=10, height=2,anchor=CENTER, font=('Ivy 25 bold'), bg=co7, fg=co1, relief=FLAT)
l_qtd.place(x=450, y=90)

l_qtd_itens = Label(frameMeio, text='Quantidade total de itens' ,anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_qtd_itens.place(x=460, y=92)
'''

# funcao para mostrar
def mostrar():
    # creating a treeview with dual scrollbars
    tabela_head = ['ID','Nome', 'Data de Nascimento', 'Nome do Pai', 'Nome da Mãe', 'Casados na Igreja', 'Padrinho', 'Madrinha']

    lista_itens = []

    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended",columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center", "center"]
    h=[40,150,100,160,130,100,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)

        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)

    quantidade = []

    for iten in lista_itens:
        quantidade.append(iten[6])


#    Total_padrinho = sum(quantidade)
#    Total_itens = len(quantidade)
#
#    l_total['text'] = 'R$ {:,.2f}'.format(Total_padrinho)
#    l_qtd['text'] = Total_itens

mostrar()

janela.mainloop()