from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys
import csv

preto = '#f0f3f5' 
branca  = '#feffff' 
hexadecimal = "#38576b" 
letra = "#403d3d"

# JANELA 

janela_principal = Tk ()
janela_principal.title = ('')
janela_principal.geometry('500x500')
janela_principal.configure(background=branca)
janela_principal.resizable(width=FALSE, height=FALSE)

estilo = Style(janela_principal)
estilo.theme_use('clam')

# ESTRUTURAS

estrutura_cima = Frame(janela_principal, width= 500, height= 50, bg =hexadecimal, relief='flat')
estrutura_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

estrutura_meio = Frame(janela_principal, width=500, height=150, bg=branca, relief='flat')
estrutura_meio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

estrutura_tabela = Frame(janela_principal, width=500, height=100, bg=branca, relief='flat')
estrutura_tabela.grid(row= 2, column=0, columnspan=2, padx=10, pady=1, sticky=NW)

# Estrutura Cima
nome = Label(estrutura_cima, text='Agenda Telefonica' , height=1, anchor=NE, font=('verdana 17 bold '), bg= hexadecimal, fg=branca )
nome.place(x=5, y=5)

# Banco de Dados
def ver_contatos():
    todos_contatos = []
    #acessando o ficheiro csv
    with open('contatos.csv') as file:
        ler_csv = csv.reader(file)
        for row in ler_csv:
            todos_contatos.append(row)
            
    return todos_contatos

# Função adiconar contatos
def adicionar_contatos(i):
    #acessando o ficheiro csv
    with open('contatos.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)
        
        
# Função remover contatos       
def remover_contatos(i):
    def adiionar_novalista(j):
        #acessando o ficheiro csv
        with open('contatos.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)
            
            
    nova_lista = []
    telefone = i

    with open('contatos.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            nova_lista.append(row)
            for campo in row:
                if campo == telefone:
                    nova_lista.remove(row)

    adiionar_novalista(nova_lista)
    
   
# Função atualizar contatos     
def atualizar_contatos(i):
    def atualizar_novalista(i):
        #acessando o ficheiro csv
        with open('contatos.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(i)
            
            
    nova_lista = []
    telefone = i[0]

    with open('contatos.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            nova_lista.append(row)
            for campo in row:
                if campo == telefone:
                    nome = i[1]
                    sexo = i[2]
                    telefone = i[3]
                    email = i[4]

                    dados = [nome, sexo, telefone, email]
                    
                    # trocando lista por index
                    index = nova_lista.index(row)
                    nova_lista[index] = dados
                    
                    print(nova_lista)

    atualizar_novalista(nova_lista)
    

# funcao procurar contatos     
def procurar_contatos(i):
    contatos = []
    telefone = i

    with open('contatos.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for campo in row:
                if campo == telefone:
                    contatos.append(row)
    
    return contatos



#Funções 
#Função Mostrar
def mostrar():

    # creating a treeview with dual scrollbars
    list_header = ['Nome', 'Sexo', 'telefone','email']

    df_list = ver_contatos()
    
    global tree

    tree = ttk.Treeview(estrutura_tabela, selectmode="extended",
                        columns=list_header, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(
        estrutura_tabela, orient="vertical", command=tree.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(
        estrutura_tabela, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["nw","nw","nw","nw","nw",]
    h=[120,50,80,120,200]
    n=0
    
    # tree cabecalho
    tree.heading(0,text='Nome', anchor=NW)
    tree.heading(1,text='Sexo', anchor=NW)
    tree.heading(2,text='Telefone', anchor=NW)
    tree.heading(3,text='Email', anchor=NW)
    
    # tree  corpo
    tree.column(0, width=120,anchor='nw')
    tree.column(1, width=50,anchor='nw')
    tree.column(2, width=100,anchor='nw')
    tree.column(0, width=120,anchor=hd[0])


    for item in df_list:
        tree.insert('', 'end', values=item)

mostrar()


def inserir():
    nome = nome.get()
    sexo = sexo.get()
    telefone = telefone.get()
    email = email.get()
    
    dados = [nome, sexo, telefone, email]
    
    if nome =='' or sexo =='' or telefone =='' or email =='':
        messagebox.showwarning('Dados','Por favor preencha todos os campos')
        
    else:
        adicionar_contatos(dados)
        messagebox.showinfo('Dados','Dados foram adicionado')
        nome.delete(0,'end')
        sexo.delete(0,'end')
        telefone.delete(0,'end')
        email.delete(0,'end')
        
        # chamar a funcao mostrar dados para atualizar a lista
        mostrar()


def atualizar():
    try:
        treev_contato = tree.focus()
        treev_dicionario = tree.item(treev_contato)
        treev_lista = treev_dicionario['values']
        
        nome = str(treev_lista[0])
        sexo = str(treev_lista[1])
        telefone = str(treev_lista[2])
        email = str(treev_lista[3])
        
        nome.insert(0,nome)
        sexo.insert(0,sexo)
        telefone.insert(0,telefone)
        email.insert(0,email)
        
        
        def confirmar():
            novo_nome = nome.get()
            novo_sexo = sexo.get()
            novo_telefone = telefone.get()
            novo_email = email.get()
            
            contatos = [telefone,novo_nome, novo_sexo, novo_telefone, novo_email]
            
            atualizar_contatos(contatos)
                
            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')
            
            nome.delete(0,'end')
            sexo.delete(0,'end')
            telefone.delete(0,'end')
            email.delete(0,'end')

            for widget in estrutura_tabela.winfo_children():
                widget.destroy()
                
            confirmar.destroy()

            mostrar()
            
        confirmar = Button(estrutura_meio,command=confirmar, text="Confirmar", width=10, height=1, bg=branca, fg=preto, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
        confirmar.place(x=290, y=110)

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')


def remover():
    
    try:
        treev_contatos = tree.focus()
        treev_dicionario = tree.item(treev_contatos)
        treev_lista = treev_dicionario['values']
        valor = str(treev_lista[2])
                
        remover_contatos(valor)
        
        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

        for widget in estrutura_tabela.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')


def procurar():
    telefone = procurar.get()
    
    contatos = procurar_contatos(telefone)
    
    def delete_command():
        tree.delete(*tree.get_children())
        
    delete_command()
    
    for item in contatos:
        tree.insert('', 'end', values=item)

# inserir informações do contato
nome = Label(estrutura_meio, text="Nome *", width=20, height=1,anchor=NW, font=('Ivy 10 '),bg=branca, fg=letra)
nome.place(x=10, y=20)
nome = Entry(estrutura_meio, width=25, justify='left',font=("",10),highlightthickness=1, relief="flat")
nome.place(x=80, y=20)

sexo = Label(estrutura_meio, text="Sexo *", height=1,anchor=NW, font=('Ivy 10 '), bg=branca, fg=letra)
sexo.place(x=10, y=50)
sexo = Combobox(estrutura_meio, width=27)
sexo['values']= ('','F','M')
sexo.place(x=80, y=50)

tel = Label(estrutura_meio, text="Telefone *", height=1,anchor=NW, font=('Ivy 10 '), bg=branca, fg=letra)
tel.place(x=10, y=80)
tel = Entry(estrutura_meio, width=25, justify='left',font=("",10),highlightthickness=1, relief="flat")
tel.place(x=80, y=80)

email = Label(estrutura_meio, text="email *", height=1,anchor=NW, font=('Ivy 10 '), bg=branca, fg=letra)
email.place(x=10, y=110)
email = Entry(estrutura_meio, width=25, justify='left',font=("",10),highlightthickness=1, relief="flat")
email.place(x=80, y=110)

# buttons
procurar = Button(estrutura_meio,command=procurar, text="Procurar", height=1, bg=branca, fg=letra, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
procurar.place(x=290, y=20)
procurar = Entry(estrutura_meio, width=16, justify='left',font=("",11),highlightthickness=1, relief="flat")
procurar.place(x=347, y=21)

ver = Button(estrutura_meio,command=mostrar, text="Ver dados",width=10, height=1, bg=branca, fg=letra, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
ver.place(x=290, y=50)

adicionar = Button(estrutura_meio,command=inserir, text="Adicionar", width=10, height=1, bg=branca, fg=letra, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
adicionar.place(x=400, y=50)

atualizar = Button(estrutura_meio,command=atualizar, text="Atualizar", width=10, height=1, bg=branca, fg=letra, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
atualizar.place(x=400, y=80)

deletar = Button(estrutura_meio,command=remover, text="Deletar", width=10, height=1, bg=branca, fg=letra, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
deletar.place(x=400, y=110)



janela_principal.mainloop()

