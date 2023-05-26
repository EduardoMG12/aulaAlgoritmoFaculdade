# A série de Fibonacci é formada pela seqüência: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ..., etc. Escreva um
# algoritmo que gere a série de Fibonacci até o vigésimo termo.

n = 20

termo1 = 1
termo2 = 1

print(termo1)
print(termo2)

for _ in range(3, n+1):
    proximo_termo = termo1 + termo2
    print(proximo_termo)
    termo1 = termo2
    termo2 = proximo_termo