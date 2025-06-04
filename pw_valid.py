# Projeto: Validador e senha
# Regras:
# A senha tem que ter no mínimo 8 caracteres
# A senha não pode ser 12345678
# O resultado esperado é dizer se a senha é válida ou não 

# Pegar senha sem exibir ao usuário o que está sendo digitado
# from getpass import getpass
# password = getpass('Digite sua senha: ')

password = input('Digite a senha: ')
# char_counter = len(password)

# if char_counter < 8 or password == '12345678':
#    print('Senha inválida!')

if len(password) < 8 or password == '12345678':
    print('Senha inválida!')
else:
    print('Senha válida!')
