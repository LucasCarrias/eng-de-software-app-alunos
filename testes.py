from classes.tasks import Tarefa
from classes.alunos import Aluno

tarefa = Tarefa()
aluno = Aluno()

aluno.sortear()


tarefa.cadastrar(aluno.nome, "Lixo", "da porra", "69")
tarefa.salvar_tarefa()


for i in tarefa.tarefas:
    print(i)
    print(type(i))

