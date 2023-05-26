# Ler um número inteiro e determinar se ele é primo. Obs. um número é primo quando for divisível
# somente por 1 e por ele mesmo.

numero = int(input("Digite um número: "))

if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print(f"{numero} não é um número primo.")
            break
    else:
        print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")