numero = int(input("Digite um Número"))
numero2 = int(input("Digite um Número"))
numero3 = int(input("Digite um Número"))
somaNegativos = 0
somaPositivos = 0
if numero < 0:
    somaNegativos += numero
else:
    somaPositivos += numero 
if numero2 < 0:
    somaNegativos += numero2
else:
    somaPositivos += numero2 
if numero3 < 0:
    somaNegativos += numero3
else:
    somaPositivos += numero3 
print("positivos:",somaPositivos)
print("negativos", somaNegativos)