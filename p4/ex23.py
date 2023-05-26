# Fulano tem 1,50 metro e cresce 2 centímetros por ano, enquanto Ciclano tem 1,10 metro e cresce 3
# centímetros por ano. Construa um algoritmo que calcule e imprima quantos anos serão necessários
# para que Ciclano seja maior que Fulano.

fulano=float(1.50)
ciclano=float(1.10)
ano=0

while(ciclano<fulano):
    fulano+=0.02
    ciclano+=0.03
    ano+=1
    
print(ano)
