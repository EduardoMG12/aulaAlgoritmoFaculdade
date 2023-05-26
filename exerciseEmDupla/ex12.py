valorTotal = str(input("Informe o valor do produto: "))
lenght = len(valorTotal) -1
ultimoNumero = valorTotal[lenght]
if ultimoNumero != 0:
    unidade = ultimoNumero
    valorTotal = int(valorTotal)
    valorTotal -= int(ultimoNumero)
valorTotal= valorTotal/10
print("você precisará de ",valorTotal," de 10R$ e ", unidade, " de 1R$.")