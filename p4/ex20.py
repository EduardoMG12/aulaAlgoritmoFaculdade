# Apresentar o fatorial de um número informado pelo usuário (ex. Fatorial de 5 = 5 * 4 * 3 * 2 * 1).
number = int(input("Digite um número: "))
calculo= 1
for i in range(2, (number + 1)):
    calculo *= i

print(f"O resultado é: {calculo}")