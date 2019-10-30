class Tarefa():

    tarefas = []
    tarefa_atual = []
    nome = ""
    descricao = ""
    data = "" 

    def __init__(self):
        self.ler_tarefas()      
    
    def cadastrar(self, nome, descricao, data, aluno_nome ="Desconhecido"):   
        self.nome = nome
        self.descricao = descricao
        self.data = data 
        self.tarefa_atual = [aluno_nome, nome, descricao, data]
        self.tarefas += [self.tarefa_atual]
        

    def salvar_tarefa(self):
        if self.tarefa_atual:        
            with open('data/tarefas.csv', 'a') as arquivo:       
                arquivo.write(','.join(self.tarefa_atual)+"\n")

    def ler_tarefas(self):
        if self.tarefas_vazias():
            try:
                with open('data/tarefas.csv', 'r') as arquivo:
                    temp = arquivo.readlines()
                    for tarefa in temp:
                        self.tarefas += [tarefa.strip().split(',')]
            except FileNotFoundError:
                file = open('data/tarefas.csv', 'x')            
                file.close()
    

    def tarefas_vazias(self):
        return self.tarefas == []
    
    def apagar_tarefa(self):
        self.tarefas = []

    def apagar_tudo(self):
        self.apagar_tarefa()
        self.apagar_arquivo()

    @staticmethod
    def apagar_arquivo():
        with open('data/tarefas.csv', 'w') as arquivo:
            arquivo.write('')
   