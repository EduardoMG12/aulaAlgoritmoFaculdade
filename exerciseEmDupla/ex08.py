import random

nome = input("Digite o seu nome: ")
sobrenome = input("Digite o seu sobrenome: ")
ano = input("Digite o seu ano de nascimento: ")

nomes = []
emails = []

for i in range(4):
    n = random.randint(100, 999)
    sobrenome_original = sobrenome
    if n < 350:
        numero = random.randint(0, 3)
        sobrenome_modificado = random.choice(sobrenome)
    else:
        sobrenome_modificado = sobrenome
    email = nome.lower() + sobrenome_modificado.lower() + str(n) + "@exemplo.com"
    emails.append(email)
    if n < 456: 
        nome_modificado = random.choice(nome)
        nomedeUsuario = nome_modificado.lower() + sobrenome_original.upper()
    else:
        sobrenome_modificado = random.choice(sobrenome)
        nomedeUsuario = nome.lower() + sobrenome_modificado.upper()
    nomes.append(nomedeUsuario)

print("Os e-mails gerados são:")
for email in emails:
    print(email)

print("Os nomes de usuário gerados são:")
for nomeUsuario in nomes:
    print(nomeUsuario)