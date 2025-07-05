# Verificar se tem 17 anos ou mais
# age = int(input('Digite sua idade.'))

# if age == 17:
#   print('Hora de se alistar!!! ')
# elif age < 17:
#   print('Cedo demais!!!')
# elif age > 17:
#    print('Tarde demais!!!')

# Projeto: Validador e senha
# Regras:
# A senha tem que ter no mínimo 8 caracteres
# A senha não pode ser 12345678
# O resultado esperado é dizer se a senha é válida ou não

# Pegar senha sem exibir ao usuário o que está sendo digitado
# from getpass import getpass
# password = getpass('Digite sua senha: ')

password = input('Digite sua senha: ')

if password == '12345678' or len(password) < 8:
    print('Senha inválida')

else:
    print('Senha válida!')

