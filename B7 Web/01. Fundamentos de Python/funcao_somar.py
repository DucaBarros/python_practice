# Função Somar

def somar(x, y):
    resultado = x + y
    return resultado

print('Calculadora')
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segudo número: '))

soma_dos_numeros = somar(numero1, numero2)
print(f'Resultado: {soma_dos_numeros}')

