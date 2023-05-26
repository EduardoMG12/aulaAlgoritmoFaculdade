# Apresentar os resultados da tabuada de um número qualquer.
numberToTable = int(input("Digite um número: "))
i = 0 

for i in range(11):
    print(f"{i} X {numberToTable} = {numberToTable * i}")

