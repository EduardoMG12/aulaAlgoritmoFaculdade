valorEmprestimo = 10000
juros = 0.02

for mes in range(1, 25):
    valorDoJurosMes = valorEmprestimo * juros
    valorEmprestimo -= valorDoJurosMes
    print(f"_____mes_{mes}______")
    print(f"{valorDoJurosMes:.2f} juros pagos")
    print(f"{valorEmprestimo:.2f} empréstimo")

ultima_parcela = valorEmprestimo
montante_pago = 10000 - valorEmprestimo

print(f"Valor da última parcela: R$ {ultima_parcela:.2f}")
print(f"Montante pago ao final do empréstimo: R$ {montante_pago:.2f}")