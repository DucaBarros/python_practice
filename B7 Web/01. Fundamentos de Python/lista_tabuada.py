# Tabuada 2.0

# Lista
lista_multiplicando = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Escolher o número e converter para inteiro
multiplicador = int(input('Digite o algarismo que deseja ver a tabuada: ')) 

# Separador/organizador
print('-----------')

# Para cada número "n" na lista multiplicar pelo número digitado "multiplicador"
for n in lista_multiplicando:
    produto = (n * multiplicador) # Multiplcando x Multiplicador
    print(f'{n} x {multiplicador} = {produto}') # Exibir a tabuada