# Fulano aplicou R$ 100,00 com rendimento de 5% ao mês. Quantos meses serão necessários para o
# capital investido ultrapasse a R$ 200,00.
investimentoFulano=100
juros=5
totalArrecado=0
ano=0
while(totalArrecado<=200):
    totalArrecado+=(investimentoFulano*(5 / 100))
    ano+=1

print(f"{ano} anos")
print(totalArecado)