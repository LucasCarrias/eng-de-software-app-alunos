import random

class Aluno():

    nome = ''
    alunos = []

    def _init(self):
        self.ler_alunos()

    def ler_alunos(self):
        if self.alunos == []:
            try:
                with open('data/alunos.csv', 'r') as arquivo:
                    temp = arquivo.readlines()
                    for aluno in temp:
                        self.alunos += [aluno.strip().split(',')]
            except FileNotFoundError:
                file = open('data/alunos.csv', 'x')         
                file.close()
    
    def sortear(self):
        self.ler_alunos()
        self.nome = random.choice(self.alunos)[0]
        
