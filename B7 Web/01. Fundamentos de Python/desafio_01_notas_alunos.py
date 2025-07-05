# Cenário:
    # Você é um desenvolvedor responsável por criar um sistema simples para uma escola. 
    # O objetivo é calcular a média das notas de uma turma 
    # e identificar quais alunos foram aprovados ou reprovados.

# Requisitos do sistema:
    # A escola tem 5 alunos.
    # Cada aluno tem 3 notas.

# O sistema deve:
    # Solicitar o nome do aluno.
    # Solicitar as 3 notas.
    # Calcular a média.
    # Informar se o aluno foi aprovado (média ≥ 7.0) ou reprovado (média < 7.0).
    # Exibir ao final um resumo com o nome, média e situação (Aprovado/Reprovado) de todos os alunos.


#Biblioteca para salvar dados de cada aluno
reg_students = []

# Solicitando nome do aluno
for n in range(1, 6):
    student = input(f'Digite o nome do aluno {n}: ')
print(reg_students)