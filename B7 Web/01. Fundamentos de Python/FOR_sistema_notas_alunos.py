#Cenário com chatGPT
# Prompt: 
    # Estou estudando python. 
    # Me dê um cenário onde eu tenha que desenvolver um algoritmo 
    # para resolver o problema utilizando a estrutura de repetição FOR

# Resposta:
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
# alunos []

# Solicitando nome do aluno
# aluno = input('Nome do aluno: ')

alunos = []

for i in range(5):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Digite a nota {j+1} de {nome}: "))
        notas.append(nota)
    
    media = sum(notas) / 3
    situacao = "Aprovado" if media >= 7 else "Reprovado"
    alunos.append((nome, media, situacao))

print("\n--- Resultado Final ---")

for aluno in alunos:
    print(f"Aluno: {aluno[0]} | Média: {aluno[1]:.2f} | Situação: {aluno[2]}")
