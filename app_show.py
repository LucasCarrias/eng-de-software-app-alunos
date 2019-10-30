from classes.tasks import Tarefa
from classes.alunos import Aluno
from tkinter import *
from random import randint
from functools import partial

janela = Tk()

def bt_click(lista):
	a = ed.get()
	if a == "1":
		sortear(lista)
	elif a == "2":
		mostrar()
	elif a == "3":
		mostar_s(lista)
	elif a == "4":
		sair()


def bt_cvoltar(sortear):
	sortear.destroy()


def sortear(lista,lista2,janela):
	alunos = []
	alunos_s=[]
	arquivo = open("alunos.txt",errors="ignore")

	for linha in arquivo:
		alunos += [linha]
	
	for i in range(len(lista)):
		if lista[i] in alunos:
			pos = alunos.index(lista[i])
			del(alunos[pos])
	aluno = alunos[randint(0,len(alunos))]
	
	lb = Label(janela,text=aluno)
	lb.place(x=240,y=480)
	armazenar(lista2,aluno)


def mostrar():
	lista = Tk()
	alunos = []
	arquivo = open("alunos.txt",errors="ignore")

	scrollbar = Scrollbar(lista)
	scrollbar.pack(side=RIGHT, fill=Y)
	listbox = Listbox(lista, yscrollcommand=scrollbar.set)

	for linha in arquivo:
		listbox.insert(END, str(linha).strip())
	listbox.pack(fill=BOTH)
	scrollbar.config(command=listbox.yview)


	lista.geometry("400x150+500+200")
	lista.minsize(width=300,height=160)
	lista.mainloop()

	
def mostar_s(lista):
	l = Tk()
	scrollbar = Scrollbar(l)
	scrollbar.pack(side=RIGHT, fill=Y)
	listbox = Listbox(l, yscrollcommand=scrollbar.set)
	for i in range(len(lista)-1,-1,-1):
		listbox.insert(END, str(lista[i]))
	listbox.pack(fill=BOTH)
	scrollbar.config(command=listbox.yview)
	l.geometry("400x150+500+200")
	l.minsize(width=300,height=160)
	l.mainloop()

def sair():
	return quit()

def armazenar(lista,nome):
	if nome in lista:
		pass
	else:
		lista += [nome]

def cancelar(classe):
	bt_cvoltar(classe)

def salvar(lista,lista2,classe):
	print(lista2)
	for i in range(len(lista2)):
		armazenar(lista,lista2[i])
	bt_cvoltar(classe)
	

def criar_tarefas(lista):
	criar_t = Tk()
	alunos = []
	
	#NOME DA TAREFA
	lb = Label(criar_t,text="Nome da Tarefa:")
	lb.config(font=("Courier", 15))
	lb.place(x=20,y=20)

	rec = Entry(criar_t,font=("Calibri",15),justify="center",bd=4)
	rec.place(x=220,y=22,width=300)

	#DATA DE ENTREGA
	lb2 = Label(criar_t,text="Data de Entrega:")
	lb2.config(font=("Courier", 15))
	lb2.place(x=20,y=60)

	data = Entry(criar_t,font=("Calibri",15),justify="center",bd=4)
	data.place(x=220,y=62,width=300)


	#DESCRIÇÃO
	lb3 = Label(criar_t,text="Descrição:")
	lb3.config(font=("Courier", 15))
	lb3.place(x=20,y=100)

	desc = Entry(criar_t,font=("Calibri",15),bd=4)
	desc.place(x=220,y=102,width=300)

	#BOTAO SORTERAR
	sort = Button(criar_t, width=20, text="Sortear alunos")
	sort["command"] = partial(sortear,lista,alunos,criar_t)
	sort.place(x=20, y=220)
	sort.bind()

	#BOTAO SALVAR
	bt1 = Button(criar_t,width=20,text="Salvar")
	bt1["command"] = partial(salvar,lista,alunos,criar_t)
	bt1.place(x=400,y=560)
	bt1["bg"] = "#90ee90"

	#BOTAO CANCELAR
	bt2 = Button(criar_t,width=20,text="Cancelar")
	bt2["command"] = partial(cancelar,criar_t)
	bt2.place(x=200,y=560)
	bt2["bg"] = "#fa7f72"

	criar_t.geometry("600x600+400+20")
	criar_t.minsize(width=600,height=400)
	criar_t.mainloop()

def menu_inicial():
	lista = []

	bt2 = Button(janela, width=40, text="1 - Listar alunos")
	bt2["command"] = partial(mostrar)
	bt2.place(x=160, y=120)

	bt3 = Button(janela, width=40, text="2 - Listar alunos sorteados")
	bt3["command"] = partial(mostar_s,lista)
	bt3.place(x=160, y=200)

	bt4 = Button(janela, width=40, text="3 - Criar Tarefa")
	bt4["command"] = partial(criar_tarefas,lista)
	bt4.place(x=160, y=280)
	'''
	bt5 = Button(janela, width=20, text="5 - Mostar Tarefas")
	bt5["command"] = partial(mostrar_tarefas)
	bt5.place(x=80, y=180)
	'''
	bt6 = Button(janela, width=20, text="6 - Sair")
	bt6["command"] = partial(sair)
	bt6.place(x=240, y=440)

	janela.geometry("600x600+400+400")
	janela.minsize(width=300,height=300)

def main():

	menu_inicial()

	janela.mainloop(0)


if __name__ == "__main__":
	main()
