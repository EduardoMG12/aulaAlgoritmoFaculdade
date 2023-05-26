# Apresentar todos os números primos entre 5 e 1700.
# Verifica se o número é divisível apenas por 1 e por ele mesmo

import math

for numero in range(5,1000000000):
    if numero > 1:
        for i in range(2, int(math.sqrt(numero))):
            if numero % i == 0:
                print(f"{numero} não é um número primo.")
                break
        else:
            print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")