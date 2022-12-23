from base64 import*
from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import*
import webbrowser
from platypus import*
import sqlite3 as lite
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import landscape

# Criando banco de dados
con = lite.connect('dados.db')
def conecta_bd():
    con = lite.connect('dados.db')

def desconecta_bd():
    con.close()

def criar_bd():
    conecta_bd()
    
    cur = con.cursor()
    cur.execute(
            "CREATE TABLE IF NOT EXISTS Cadastro (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, data_de_nasc DATE, nome_pai TEXT, nome_mae TEXT, casados TEXT, padrinho TEXT, madrinha TEXT, celebrante TEXT, dia_batismo DATE)"
            )

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
        query = "UPDATE Cadastro SET nome=?, data_de_nasc=?, nome_pai=?, nome_mae=?, casados=?, padrinho=?, madrinha=?, celebrante=?, dia_batismo=? WHERE id=?"
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

# sys.setrecursionlimit(10000) # Configuracao do limite de recursao para 10000

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

janela.geometry('950x700')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

################# Frames ####################
###########-> DEIXAR RESPONSIVO <-###########

frameCima = Frame(janela, width=950, height=60, bg=co1, pady=0, padx=50,  relief="flat")
frameCima.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

frameMeio = Frame(janela, width=950, height=305,bg=co1, pady=10, padx=50, relief="flat")
frameMeio.grid(row=1, column=0,pady=1, padx=0, sticky=NSEW)

frameBotoes = Frame(janela, width=950, height=80, pady=0, padx=95, bg=co1, relief="flat")
frameBotoes.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)
#frameBotoes.place(relx=0.1,rely=0.1, relwidth=0.5,relheight=0.5)

frameBottom = Frame(janela,width=950, height=280,bg=co1, relief="flat")
frameBottom.grid(row=3, column=0, pady=0, padx=1, sticky=NSEW)

################## Cabecalho do programa #####################

app_logo = Label(frameCima, image='', text="Cadastro Batismo", width=900, compound=LEFT, relief="flat", anchor=NW, font=('Verdana 20 bold'),bg=co1, fg=co4)
app_logo.place(x=30, y=8)

app_img = Image.open('main_files\icon\icon_logo.png')
app_img = app_img.resize((280, 280))
app_img = ImageTk.PhotoImage(app_img)

img_logo = Label(frameMeio, image=app_img, text=" ", width=900, compound=CENTER, relief="flat", anchor=NW,bg=co1)
img_logo.place(x=550, y=0)

global tree

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

        #valor = treev_lista[0]

        e_nome.delete(0, 'end')
        e_nasc.delete(0, 'end')
        e_nome_pai.delete(0, 'end')
        e_nome_mae.delete(0, 'end')
        e_casados.set('Sim')
        e_padrinho.delete(0, 'end')
        e_madrinha.delete(0, 'end')
        e_celebrante.delete(0, 'end')
        e_dia_batismo.delete(0, 'end')

        id = int(treev_lista[0])
        e_nome.insert(0, treev_lista[1])
        e_nasc.insert(0, treev_lista[2])
        e_nome_pai.insert(0, treev_lista[3])
        e_nome_mae.insert(0, treev_lista[4])
        e_casados.get()
        e_casados.insert(0, treev_lista[5])
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
            e_casados.set('Sim')
            e_padrinho.delete(0, 'end')
            e_madrinha.delete(0, 'end')
            e_celebrante.delete(0, 'end')
            e_dia_batismo.delete(0, 'end')

            func_edit.destroy()
            blank_tree.destroy()
            blank_buttons.destroy()
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
            e_casados.set('Sim')
            e_padrinho.delete(0, 'end')
            e_madrinha.delete(0, 'end')
            e_celebrante.delete(0, 'end')
            e_dia_batismo.delete(0, 'end')
            
            messagebox.showinfo('Cancelado com sucesso', 'Edição cancelada. Os dados de cadastro não foram alterados.')
            
            func_edit.destroy()
            blank_tree.destroy()
            blank_buttons.destroy()
            botao_confirmar.destroy()
            botao_cancelar.destroy()        

        func_edit = Label(frameCima, text="Edição de Cadastro", width=900, compound=LEFT, relief="flat", anchor=NW, font=('Verdana 20 bold'),bg=co1, fg=co4)
        func_edit.place(x=30, y=8)
        
        blank_tree = Image.open('main_files\icon\img_blank.png')
        blank_tree = blank_tree.resize((80, 280))
        blank_tree = ImageTk.PhotoImage(blank_tree)

        blank_tree = Label(frameBottom, image=blank_tree, text=" ", width=950, compound=CENTER, relief="flat", anchor=NW,bg=co1)
        blank_tree.place(x=1, y=1)

        blank_buttons = Image.open('main_files\icon\img_blank.png')
        blank_buttons = blank_buttons.resize((80, 80))
        blank_buttons = ImageTk.PhotoImage(blank_buttons)

        blank_buttons = Label(frameBotoes, image=blank_buttons, text="", width=400, compound=LEFT, relief="flat", anchor=NW,bg=co1)
        blank_buttons.place(x=380, y=11) # x=150 provisorio, tam real x=380

        botao_confirmar = Button(frameBotoes, image=img_done, compound=LEFT, anchor=NW, text="   Salvar", width=150, overrelief=RIDGE,  font=('ivy 10 bold'),bg=co11, fg=co1, command=update)
        botao_confirmar.place(x=20, y=11)
        
        botao_cancelar = Button(frameBotoes, image=img_cancel, compound=LEFT, anchor=NW, text="   Cancelar", width=150, overrelief=RIDGE,  font=('ivy 10 bold'),bg=co10, fg=co1, command=cancelar)
        botao_cancelar.place(x=200, y=11)

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

# funcao relatorios (gerar relatorios)
def relatorios():
    
    app_logo2 = Label(frameCima, image='', text="Relatorios", width=900, compound=LEFT, relief="flat", anchor=NW, font=('Verdana 20 bold'),bg=co1, fg=co4)
    app_logo2.place(x=30, y=8)
    
    frameRel = Frame(janela, width=950, height=305, pady=0, padx=30, bg=co1, relief="flat")
    frameRel.place(relx=0,rely=0.1, relwidth=1,relheight=0.9)
    
    frameBottomRel = Frame(janela,width=950, height=395,bg=co1, relief="flat")
    frameBottomRel.grid(row=3, column=0, pady=0, padx=1, sticky=NSEW)
    
    l_nome = Label(frameRel, text="Nome", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_nome.place(x=0, y=10)
    e_nome2 = Entry(frameRel, width=40, justify='left',relief="solid", state='normal')
    e_nome2.place(x=150, y=11)
    
    l_nasc = Label(frameRel, text="Data de Nascimento", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_nasc.place(x=0+425, y=10) # y=40
    e_nasc2 = DateEntry(frameRel, width=12, background='darkblue', foreground='white', borderwidth=2, year=2022, date_pattern="dd/mm/y")
    e_nasc2.place(x=150+425, y=11) #Y=41

    l_nome_pai = Label(frameRel, text="Pai", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_nome_pai.place(x=0, y=40) # y=70
    e_nome_pai2 = Entry(frameRel, width=40, justify='left',relief="solid")
    e_nome_pai2.place(x=150, y=41) # y=71

    l_nome_mae = Label(frameRel, text="Mãe", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_nome_mae.place(x=0+425, y=40) # y=100
    e_nome_mae2 = Entry(frameRel, width=40, justify='left',relief="solid")
    e_nome_mae2.place(x=150+425, y=41) # y=101

    l_casados = Label(frameRel, text="Casados na Igreja", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_casados.place(x=0, y=70) # y=130

    list_cb = ['Sim', 'Não']
    e_casados2 = ttk.Combobox(frameRel, width=10, values = list_cb, state='readonly')
    e_casados2.set('Sim')
    e_casados2.place(x=150, y=71) # y=131

    l_padrinho = Label(frameRel, text="Padrinho", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_padrinho.place(x=0, y=100) # y=160
    e_padrinho2 = Entry(frameRel, width=40, justify='left',relief="solid")
    e_padrinho2.place(x=150, y=101) # y=161

    l_madrinha = Label(frameRel, text="Madrinha", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_madrinha.place(x=0+425, y=100) # y=190
    e_madrinha2 = Entry(frameRel, width=40, justify='left',relief="solid")
    e_madrinha2.place(x=150+425, y=101) # y=191

    l_celebrante = Label(frameRel, text="Celebrante", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_celebrante.place(x=0, y=160-30) # y=220
    e_celebrante2 = Entry(frameRel, width=40, justify='left',relief="solid")
    e_celebrante2.place(x=150, y=161-30) # y=221

    l_dia_batismo = Label(frameRel, text="Dia do Batismo", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_dia_batismo.place(x=0+425, y=160-30) # y=250
    e_dia_batismo2 = DateEntry(frameRel, width=12, background='darkblue', foreground='white', borderwidth=2, year=2022, date_pattern="dd/mm/y")
    e_dia_batismo2.place(x=150+425, y=161-30)  # y=251
    
    # funcao voltar menu
    def voltar():

        app_logo2.destroy()
        frameRel.destroy()
        botao_voltar.destroy()
        botao_rel_ind.destroy()
        frameBottomRel.destroy()
        tree2.destroy()

    # funcao buscar
    def buscar():
        tree2.delete(*tree2.get_children())
        
        lista_itens = []
        
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Cadastro WHERE dia_batismo LIKE '%"+e_dia_batismo2.get()+"%' order by ID")
            rows = cur.fetchall()
            for row in rows:
                lista_itens.append(row)
        
        count = 0
        for items in lista_itens:
            tree2.insert(parent='', index='end', iid = count, values=(items[0], items[1], items[2], items[3], items[4], items[5], items[6], items[7], items[8], items[9]))
            count += 1
    
    ####################### CRIAR FUNCAO LIMPAR CAMPOS DE BUSCA #######################
    
    # funcao atualizar campos
    def atualizar_rel():
        try:
            treev_dados = tree2.focus()
            treev_dicionario = tree2.item(treev_dados)
            treev_lista = treev_dicionario['values']

            e_nome2.delete(0, 'end')
            e_nasc2.delete(0, 'end')
            e_nome_pai2.delete(0, 'end')
            e_nome_mae2.delete(0, 'end')
            e_casados2.set('Sim')
            e_padrinho2.delete(0, 'end')
            e_madrinha2.delete(0, 'end')
            e_celebrante2.delete(0, 'end')
            e_dia_batismo2.delete(0, 'end')

            id = int(treev_lista[0])
            e_nome2.insert(0, treev_lista[1])
            e_nasc2.insert(0, treev_lista[2])
            e_nome_pai2.insert(0, treev_lista[3])
            e_nome_mae2.insert(0, treev_lista[4])
            e_casados2.get()
            e_casados2.insert(0, treev_lista[5])
            e_padrinho2.insert(0, treev_lista[6])
            e_madrinha2.insert(0, treev_lista[7])
            e_celebrante2.insert(0, treev_lista[8])
            e_dia_batismo2.insert(0, treev_lista[9])
            
        except IndexError:
            messagebox.showerror('Erro', 'Seleciona um dos registros na tabela')
    
    # funcao abrir relatorio individual
    def abrir_relatorio_ind():
        webbrowser.open("CadastroInd.pdf")
    
    # funcao gerar relatorio individual
    def criar_relatorio_ind():
        pdf = canvas.Canvas("CadastroInd.pdf")
        
        nomeRel = e_nome2.get()
        nascRel = e_nasc2.get()
        nomepaiRel = e_nome_pai2.get()
        nomemaeRel = e_nome_mae2.get()
        casadosRel = e_casados2.get()
        padrinhoRel = e_padrinho2.get()
        madrinhaRel = e_madrinha2.get()
        celebranteRel = e_celebrante2.get()
        dia_batismoRel = e_dia_batismo2.get()
        
        if nomeRel == "":
            messagebox.showerror('Erro', 'Seleciona um dos registros na tabela e aperte no botão "Atualizar" para gerar o relatório desejado')
        else:
            pdf.drawImage("main_files\icon\icon_logo.PNG", x=240, y=700, anchor=LEFT, width=100, height=100, mask="auto")
            pdf.setFont("Helvetica-Bold", 12)
            pdf.drawString(100+100, 660, 'COMPROVANTE DE BATISMO')
            pdf.setFont("Helvetica", 10)
            pdf.drawString(80, 650-30, 'Diocese de Palmeira dos Índios')
            pdf.drawString(80, 630-30, 'Paróquia de Nossa Senhora do Rosário')
            pdf.drawString(80, 610-30, 'Praça da Matriz, S/N - CENTRO')
            pdf.drawString(80, 590-30, 'CEP 57.545-000, AL')
            pdf.drawString(80, 570-30, 'TEL (82) 98103-2993')
            
            pdf.rect(50, 500, 500, 1, fill=False, stroke=True)
            
            pdf.setFont("Helvetica-Bold", 10)
            pdf.drawString(60+20, 500-50, 'Nome: ')
            pdf.drawString(320+20, 500-50, 'Data de Nascimento: ') # 650
            pdf.drawString(60+20, 450-50, 'Pai: ') # 600
            pdf.drawString(320+20, 450-50, 'Mãe: ') # 550
            pdf.drawString(60+20, 400-50, 'Casados: ') # 500
            pdf.drawString(60+20, 350-50, 'Padrinho: ') # 450
            pdf.drawString(320+20, 350-50, 'Madrinha: ') # 400
            pdf.drawString(60+20, 300-50, 'Celebrante: ') # 350
            pdf.drawString(320+20, 300-50, 'Dia do Batismo: ') # 300
            
            pdf.setFont("Helvetica", 8)
            pdf.drawString(60+20, 470-40, nomeRel)
            pdf.drawString(320+20, 470-40, nascRel) # 620+10
            pdf.drawString(60+20, 420-40, nomepaiRel) # 570+10
            pdf.drawString(320+20, 420-40, nomemaeRel) # 520+10
            pdf.drawString(60+20, 370-40, casadosRel)# 470+10
            pdf.drawString(60+20, 320-40, padrinhoRel)# 420+10
            pdf.drawString(320+20, 320-40, madrinhaRel)# 370+10
            pdf.drawString(60+20, 270-40, celebranteRel)# 320+10
            pdf.drawString(320+20, 270-40, dia_batismoRel)# 270+10
            
            pdf.showPage()
            pdf.save()
            
            messagebox.showinfo('Sucesso', 'Relatorio gerado com sucesso')
            
            # Abre o navegador padrao exibindo o relatorio:
            abrir_relatorio_ind()
    
    # funcao abrir relatorio geral
    def abrir_relatorio_ger():
        webbrowser.open("CadastroGer.pdf")
    
    # funcao abrir multiplos individuais
    def abrir_mult_rel_ind():
        webbrowser.open("CadastroMultInd.pdf")
    
    # funcao gerar multiplos individuais
    def criar_mult_rel_ind():
        
        pdf = canvas.Canvas("CadastroMultInd.pdf")
        
        lista_itens = []
        
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Cadastro WHERE dia_batismo LIKE '%"+e_dia_batismo2.get()+"%' order by ID")
            
            rows = cur.fetchall()
            for row in rows:
                lista_itens.append(row)
                
        linha = 440+70
        linhaDiv = 393+40+70
        for items in lista_itens:
            linha = linha - 20
            linhaDiv = linhaDiv - 20
            
            pdf.setFont("Helvetica", 9)
            pdf.drawImage("main_files\icon\icon_logo.PNG", x=240, y=700, anchor=LEFT, width=100, height=100, mask="auto")
            pdf.setFont("Helvetica-Bold", 12)
            pdf.drawString(100+100, 660, 'COMPROVANTE DE BATISMO')
            pdf.setFont("Helvetica", 10)
            pdf.drawString(80, 650-30, 'Diocese de Palmeira dos Índios')
            pdf.drawString(80, 630-30, 'Paróquia de Nossa Senhora do Rosário')
            pdf.drawString(80, 610-30, 'Praça da Matriz, S/N - CENTRO')
            pdf.drawString(80, 590-30, 'CEP 57.545-000, AL')
            pdf.drawString(80, 570-30, 'TEL (82) 98103-2993')
            
            pdf.rect(50, 500, 500, 1, fill=False, stroke=True)
            
            pdf.setFont("Helvetica-Bold", 10)
            pdf.drawString(60+20, 500-50, 'Nome: ')
            pdf.drawString(320+20, 500-50, 'Data de Nascimento: ') # 650
            pdf.drawString(60+20, 450-50, 'Pai: ') # 600
            pdf.drawString(320+20, 450-50, 'Mãe: ') # 550
            pdf.drawString(60+20, 400-50, 'Casados: ') # 500
            pdf.drawString(60+20, 350-50, 'Padrinho: ') # 450
            pdf.drawString(320+20, 350-50, 'Madrinha: ') # 400
            pdf.drawString(60+20, 300-50, 'Celebrante: ') # 350
            pdf.drawString(320+20, 300-50, 'Dia do Batismo: ') # 300
            
            pdf.setFont("Helvetica", 8)
            pdf.drawString(60+20, 470-40, "{nome}".format(nome=items[1]))
            pdf.drawString(320+20, 470-40, "{nasc}".format(nasc=items[2])) # 620+10
            pdf.drawString(60+20, 420-40, "{pai}".format(pai=items[3])) # 570+10
            pdf.drawString(320+20, 420-40, "{mae}".format(mae=items[4]) ) # 520+10
            pdf.drawString(60+20, 370-40, "{cas}".format(cas=items[5]))# 470+10
            pdf.drawString(60+20, 320-40, "{pad}".format(pad=items[6]))# 420+10
            pdf.drawString(320+20, 320-40, "{mad}".format(mad=items[7]))# 370+10
            pdf.drawString(60+20, 270-40, "{cel}".format(cel=items[8]))# 320+10
            pdf.drawString(320+20, 270-40, "{bat}".format(bat=items[9]))# 270+10
            pdf.showPage()
        pdf.save()
        
        messagebox.showinfo('Sucesso', 'Relatorios gerados com sucesso')
        
        # Abre o navegador padrao exibindo o relatorio:
        abrir_mult_rel_ind()
        
    # funcao gerar relatorio geral
    def criar_rel_ger():
        ''' 
        pdf = canvas.Canvas("CadastroGer.pdf", pagesize=landscape(A4))
        
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(320,550, 'RELATÓRIO GERAL DE BATISMO')
        pdf.rect(x=180, y=460+70, width=500, height=1, fill=False, stroke=True)
        pdf.setFont("Helvetica", 8)
        
        lista_itens = []
        
        with con:
            databtsm = e_dia_batismo2.get()
            cur = con.cursor()
            cur.execute("SELECT * FROM Cadastro WHERE dia_batismo LIKE '%"+e_dia_batismo2.get()+"%' order by ID")
            pdf.setFont("Helvetica", 9)
            if databtsm == "":
                databtsm = "Geral"
                
            pdf.drawString(50, 550, 'Data dos batizados: {bat}'.format(bat=databtsm))
            
            pdf.setFont("Helvetica-Bold", 7)
            pdf.drawString(50, 440+70, 'ID')
            pdf.drawString(100, 440+70, 'Nome')
            pdf.drawString(170, 440+70, 'Nascimento')
            pdf.drawString(250, 440+70, 'Nome do Pai')
            pdf.drawString(320, 440+70, 'Nome da Mãe')
            pdf.drawString(395, 440+70, 'Casados na Igreja')
            pdf.drawString(480, 440+70, 'Padrinho')
            pdf.drawString(550, 440+70, 'Madrinha')
            pdf.drawString(650, 440+70, 'Celebrante')
            pdf.drawString(730, 440+70, 'Data do Batismo')
            
            rows = cur.fetchall()
            for row in rows:
                lista_itens.append(row)
                
        linha = 440+70
        linhaDiv = 393+40+70
        count = 0
        for items in lista_itens:
            linha = linha - 20
            linhaDiv = linhaDiv - 20
            count += 1
            pdf.setFont("Helvetica", 7)
            pdf.drawString(20, linha, "{count}".format(count=count))
            pdf.drawString(50, linha, "{nome}".format(nome=items[1]))
            pdf.drawString(170, linha, "{nasc}".format(nasc=items[2]))
            pdf.drawString(220, linha, "{pai}".format(pai=items[3]))
            pdf.drawString(320, linha, "{mae}".format(mae=items[4]))
            pdf.drawString(420, linha, "{cas}".format(cas=items[5]))
            pdf.drawString(450, linha, "{pad}".format(pad=items[6]))
            pdf.drawString(550, linha, "{mad}".format(mad=items[7]))
            pdf.drawString(650, linha, "{cel}".format(cel=items[8]))
            pdf.drawString(750, linha, "{bat}".format(bat=items[9]))
            pdf.rect(x=50, y=linhaDiv, width=735, height=0.1, fill=False, stroke=True)
            
        pdf.showPage()
        pdf.save()
        '''
        ######## MODELO 2 #######
        
        pdf = canvas.Canvas("CadastroGer.pdf", pagesize=A4)
        
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(220, 780, 'RELATÓRIO GERAL DE BATISMO')
        pdf.rect(x=50, y=750, width=500, height=1, fill=False, stroke=True)
        pdf.setFont("Helvetica", 7)
        
        lista_itens = []
        
        def pag01():
        
            with con:
                cur = con.cursor()
                
                #databtsm = e_dia_batismo2.get()
                #cur.execute("SELECT * FROM Cadastro WHERE dia_batismo LIKE '%"+e_dia_batismo2.get()+"%' order by ID")
                #pdf.setFont("Helvetica", 8)
                #
                #if databtsm == "":
                #    databtsm = "Geral"
                #    
                #pdf.drawString(50, 780, 'Data dos batizados: {bat}'.format(bat=databtsm))
                
                cur.execute("SELECT * FROM Cadastro WHERE id BETWEEN 0 AND 14")
                rows = cur.fetchall()
                for row in rows:
                    lista_itens.append(row)
                    
            linha = 780
            linhaDiv = 740
            
            count = 0
            
            for items in lista_itens:
                linha = linha - 50
                linhaDiv = linhaDiv - 50
                count += 1
                
                pdf.setFont("Helvetica-Bold", 6)
                pdf.drawString(50, linha, 'ID:')
                pdf.setFont("Helvetica", 6)
                pdf.drawString(60, linha, "{count}".format(count=count))
                pdf.setFont("Helvetica-Bold", 6)
                pdf.drawString(70, linha, 'Nome:')
                pdf.setFont("Helvetica", 6)
                pdf.drawString(95, linha, "{nome}".format(nome=items[1]))
                pdf.setFont("Helvetica-Bold", 6)
                pdf.drawString(260, linha, 'Nascimento:')
                pdf.setFont("Helvetica", 6)
                pdf.drawString(300, linha, "{nasc}".format(nasc=items[2]))
                pdf.setFont("Helvetica-Bold", 6)
                pdf.drawString(340, linha, 'Pai:')
                pdf.setFont("Helvetica", 6)
                pdf.drawString(380, linha, "{pai}".format(pai=items[3]))
                pdf.setFont("Helvetica-Bold", 6)
                pdf.drawString(70, linha-10, 'Mãe:')
                pdf.setFont("Helvetica", 6)
                pdf.drawString(95, linha-10, "{mae}".format(mae=items[4]))
                pdf.setFont("Helvetica-Bold", 6)
                pdf.drawString(255, linha-10, 'Casados na Igreja:')
                pdf.setFont("Helvetica", 6)
                pdf.drawString(315, linha-10, "{cas}".format(cas=items[5]))
                pdf.setFont("Helvetica-Bold", 6)
                pdf.drawString(340, linha-10, 'Padrinho:')
                pdf.setFont("Helvetica", 6)
                pdf.drawString(380, linha-10, "{pad}".format(pad=items[6]))
                pdf.setFont("Helvetica-Bold", 6)
                pdf.drawString(70, linha-20, 'Madrinha:')
                pdf.setFont("Helvetica", 6)
                pdf.drawString(100, linha-20, "{mad}".format(mad=items[7]))
                pdf.setFont("Helvetica-Bold", 6)
                pdf.drawString(270, linha-20, 'Celebrante:')
                pdf.setFont("Helvetica", 6)
                pdf.drawString(305, linha-20, "{cel}".format(cel=items[8]))
                pdf.setFont("Helvetica-Bold", 6)
                pdf.drawString(430, linha-20, 'Data do Batismo:')
                pdf.setFont("Helvetica", 6)
                pdf.drawString(500-15, linha-20, "{bat}".format(bat=items[9]))
                
                pdf.rect(x=50, y=linhaDiv+10, width=500, height=0.1, fill=False, stroke=True)
                
            pdf.showPage()
            
        
        def pag02():
            
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Cadastro WHERE id BETWEEN 14 AND 28")
                
                rows = cur.fetchall()
                for row in rows:
                    lista_itens.append(row)
                    
            linha = 780 + 50
            linhaDiv = 740 + 50
            count = 14
            for items in lista_itens:
                linha = linha - 50
                linhaDiv = linhaDiv - 50
                count += 1
                
                pdf.setFont("Helvetica-Bold", 6)
                pdf.drawString(50, linha, 'ID:')
                pdf.setFont("Helvetica", 6)
                pdf.drawString(60, linha, "{count}".format(count=count))
                pdf.setFont("Helvetica-Bold", 6)
                pdf.drawString(70, linha, 'Nome:')
                pdf.setFont("Helvetica", 6)
                pdf.drawString(95, linha, "{nome}".format(nome=items[1]))
                pdf.setFont("Helvetica-Bold", 6)
                pdf.drawString(260, linha, 'Nascimento:')
                pdf.setFont("Helvetica", 6)
                pdf.drawString(300, linha, "{nasc}".format(nasc=items[2]))
                pdf.setFont("Helvetica-Bold", 6)
                pdf.drawString(340, linha, 'Pai:')
                pdf.setFont("Helvetica", 6)
                pdf.drawString(380, linha, "{pai}".format(pai=items[3]))
                pdf.setFont("Helvetica-Bold", 6)
                pdf.drawString(70, linha-10, 'Mãe:')
                pdf.setFont("Helvetica", 6)
                pdf.drawString(95, linha-10, "{mae}".format(mae=items[4]))
                pdf.setFont("Helvetica-Bold", 6)
                pdf.drawString(255, linha-10, 'Casados na Igreja:')
                pdf.setFont("Helvetica", 6)
                pdf.drawString(315, linha-10, "{cas}".format(cas=items[5]))
                pdf.setFont("Helvetica-Bold", 6)
                pdf.drawString(340, linha-10, 'Padrinho:')
                pdf.setFont("Helvetica", 6)
                pdf.drawString(380, linha-10, "{pad}".format(pad=items[6]))
                pdf.setFont("Helvetica-Bold", 6)
                pdf.drawString(70, linha-20, 'Madrinha:')
                pdf.setFont("Helvetica", 6)
                pdf.drawString(100, linha-20, "{mad}".format(mad=items[7]))
                pdf.setFont("Helvetica-Bold", 6)
                pdf.drawString(270, linha-20, 'Celebrante:')
                pdf.setFont("Helvetica", 6)
                pdf.drawString(305, linha-20, "{cel}".format(cel=items[8]))
                pdf.setFont("Helvetica-Bold", 6)
                pdf.drawString(430, linha-20, 'Data do Batismo:')
                pdf.setFont("Helvetica", 6)
                pdf.drawString(500-15, linha-20, "{bat}".format(bat=items[9]))
                
                pdf.rect(x=50, y=linhaDiv+10, width=500, height=0.1, fill=False, stroke=True)
                
            pdf.showPage()
            
        pag01()
        print(lista_itens)
        
        lista_itens.clear()
        print(lista_itens)
        
        pag02()
        print(lista_itens)
        
        pdf.save()
        messagebox.showinfo('Sucesso', 'Relatorio gerado com sucesso')
        # Abre o navegador padrao exibindo o relatorio:
        abrir_relatorio_ger()
    
    # botao voltar
    botao_voltar = Button(frameRel, image=img_back, compound=LEFT, anchor=NW, text="   Voltar", width=150, overrelief=RIDGE,  font=('ivy 10'),bg=co1, fg=co0, command=voltar)
    botao_voltar.place(x=40, y=200+10)

    # botao atualizar
    botao_atualizarRel = Button(frameRel, image=img_update, compound=LEFT, anchor=NW, text="   Atualizar", width=150, overrelief=RIDGE,  font=('ivy 10'),bg=co1, fg=co0, command=atualizar_rel)
    botao_atualizarRel.place(x=40, y=280)
    
    # botao relatorio ind.
    botao_rel_ind = Button(frameRel, image=img_botao_rel, compound=LEFT, anchor=NW, text="   Relatorio Individual", width=235, overrelief=RIDGE,  font=('ivy 10'),bg=co1, fg=co0, command=criar_relatorio_ind)
    botao_rel_ind.place(x=600, y=200)
    
    # botao multiplos relatorios individuais
    botao_mult_rel_ind = Button(frameRel, image=img_botao_rel, compound=LEFT, anchor=NW, text="   Multiplos Relatorios Individuais", width=235, overrelief=RIDGE,  font=('ivy 10'),bg=co1, fg=co0, command=criar_mult_rel_ind)
    botao_mult_rel_ind.place(x=600, y=250)
    
    # botao relatorio geral
    botao_rel = Button(frameRel, image=img_botao_rel, compound=LEFT, anchor=NW, text="   Relatorio Geral", width=235, overrelief=RIDGE,  font=('ivy 10'),bg=co1, fg=co0, command=criar_rel_ger)
    botao_rel.place(x=600, y=300)
    
    # botao buscar
    botao_buscar = Button(frameRel, image=img_update, compound=LEFT, anchor=NW, text="   Buscar", width=150, overrelief=RIDGE,  font=('ivy 10'),bg=co1, fg=co0, command=buscar)
    botao_buscar.place(x=320, y=200+10)
    
    def mostrar2():
        # creating a treeview with dual scrollbars
        tabela_head = ['#ID','Nome', 'Data de Nascimento', 'Nome do Pai', 'Nome da Mãe', 'Casados na Igreja', 'Padrinho', 'Madrinha', 'Celebrante', 'Dia do Batismo']
        
        global tree2, id
        
        tree2 = ttk.Treeview(frameBottomRel, selectmode="extended",columns=tabela_head, show="headings")
        
        # vertical scrollbar
        vsb = ttk.Scrollbar(frameBottomRel, orient="vertical", command=tree2.yview)
        
        # horizontal scrollbar
        hsb = ttk.Scrollbar(frameBottomRel, orient="horizontal", command=tree2.xview)
        
        tree2.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree2.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')
        frameBottomRel.grid_rowconfigure(0, weight=12)
        
        h=[30,100,100,100,100,100,100,100,100,100]
        mh=[30,100,100,100,100,100,100,100,100,100]
        n=0
        
        for col in tabela_head:
            tree2.heading(col, text=col.title(), anchor=CENTER)
            
            # adjust the column's width to the header string
            tree2.column(col, width=h[n],minwidth=mh[n],anchor=CENTER)
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
            tree2.insert(parent='', index='end', iid = count, values=(items[0], items[1], items[2], items[3], items[4], items[5], items[6], items[7], items[8], items[9]))
            count += 1
    
    mostrar2()
    
    # restaurar pesquisa
    botao_resBuscar = Button(frameRel, image=img_update, compound=LEFT, anchor=NW, text="   Restaurar Pesquisa", width=230, overrelief=RIDGE,  font=('ivy 10'),bg=co1, fg=co0, command=mostrar2)
    botao_resBuscar.place(x=280, y=280)

####################### VARIAVEIS DE ENTRADA #######################

l_nome = Label(frameMeio, text="Nome", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=20, y=10)
e_nome = Entry(frameMeio, width=40, justify='left',relief="solid")
e_nome.place(x=150+10, y=11)

l_nasc = Label(frameMeio, text="Data de Nascimento", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nasc.place(x=20, y=40)
e_nasc = DateEntry(frameMeio, width=12, background='darkblue', foreground='white', borderwidth=2, year=2022, date_pattern="dd/mm/y")
e_nasc.place(x=160, y=41)

l_nome_pai = Label(frameMeio, text="Pai", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome_pai.place(x=20, y=70)
e_nome_pai = Entry(frameMeio, width=40, justify='left',relief="solid")
e_nome_pai.place(x=150+10, y=71)

l_nome_mae = Label(frameMeio, text="Mãe", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome_mae.place(x=20, y=100)
e_nome_mae = Entry(frameMeio, width=40, justify='left',relief="solid")
e_nome_mae.place(x=150+10, y=101)

l_casados = Label(frameMeio, text="Casados na Igreja", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_casados.place(x=20, y=130)

list_cb = ['Sim', 'Não']
e_casados = ttk.Combobox(frameMeio, width=10, values = list_cb, state='readonly')
e_casados.set('Sim')
e_casados.place(x=150+10, y=131)

l_padrinho = Label(frameMeio, text="Padrinho", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_padrinho.place(x=20, y=160)
e_padrinho = Entry(frameMeio, width=40, justify='left',relief="solid")
e_padrinho.place(x=150+10, y=161)

l_madrinha = Label(frameMeio, text="Madrinha", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_madrinha.place(x=20, y=190)
e_madrinha = Entry(frameMeio, width=40, justify='left',relief="solid")
e_madrinha.place(x=150+10, y=191)

l_celebrante = Label(frameMeio, text="Celebrante", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_celebrante.place(x=20, y=220)
e_celebrante = Entry(frameMeio, width=40, justify='left',relief="solid")
e_celebrante.place(x=150+10, y=221)

l_dia_batismo = Label(frameMeio, text="Dia do Batismo", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_dia_batismo.place(x=20, y=250)
e_dia_batismo = DateEntry(frameMeio, width=12, background='darkblue', foreground='white', borderwidth=2, year=2022, date_pattern="dd/mm/y")
e_dia_batismo.place(x=150+10, y=251)

# Botao Inserir
img_add = Image.open('main_files\icon\icon_add.png')
img_add = img_add.resize((50, 50))
img_add = ImageTk.PhotoImage(img_add)

botao_inserir = Button(frameBotoes, image=img_add, compound=LEFT, anchor=NW, text="   Cadastrar", width=150, overrelief=RIDGE,  font=('ivy 10'),bg=co1, fg=co0, command=inserir)
botao_inserir.place(x=20, y=11)

# Botao Atualizar/Editar
img_done = Image.open('main_files\icon\icon_done.png')
img_done = img_done.resize((50, 50))
img_done = ImageTk.PhotoImage(img_done)

img_cancel = Image.open('main_files\icon\icon_cancel.png')
img_cancel = img_cancel.resize((50, 50))
img_cancel = ImageTk.PhotoImage(img_cancel)

img_edit = Image.open('main_files\icon\icon_edit.png')
img_edit = img_edit.resize((50, 50))
img_edit = ImageTk.PhotoImage(img_edit)

botao_atualizar = Button(frameBotoes, image=img_edit, compound=LEFT, anchor=NW, text="   Editar", width=150, overrelief=RIDGE,  font=('ivy 10'),bg=co1, fg=co0, command=atualizar)
botao_atualizar.place(x=200, y=11)

# Botao Deletar
img_delete  = Image.open('main_files\icon\icon_delete.png')
img_delete = img_delete.resize((50, 50))
img_delete = ImageTk.PhotoImage(img_delete)

botao_deletar = Button(frameBotoes, image=img_delete, compound=LEFT, anchor=NW, text="   Excluir", width=150, overrelief=RIDGE,  font=('ivy 10'),bg=co1, fg=co0, command=deletar)
botao_deletar.place(x=380, y=11)

# Botao ver Registros
img_back = Image.open('main_files\icon\icon_goback.png')
img_back = img_back.resize((50, 50))
img_back = ImageTk.PhotoImage(img_back)

img_botao_rel  = Image.open('main_files\icon\icon_export.png')
img_botao_rel = img_botao_rel.resize((40, 40))
img_botao_rel = ImageTk.PhotoImage(img_botao_rel)

img_item  = Image.open('main_files\icon\icon_item.png')
img_item = img_item.resize((50, 50))
img_item = ImageTk.PhotoImage(img_item)

img_update  = Image.open('main_files\icon\icon_update.png')
img_update = img_update.resize((50, 50))
img_update = ImageTk.PhotoImage(img_update)

botao_ver = Button(frameBotoes, image=img_item, compound=LEFT, anchor=NW, text="   Registros", width=150, overrelief=RIDGE,  font=('ivy 10'),bg=co1, fg=co0, command=relatorios)
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

criar_bd()
mostrar()

janela.mainloop()