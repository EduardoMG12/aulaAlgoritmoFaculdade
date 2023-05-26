# Apresentar todos os números primos entre 5 e 1700.
# Verifica se o número é divisível apenas por 1 e por ele mesmo

import random

for numero in range(5,100):
   alt = random.randint(0, 1)
   if alt ==0:
      print(True)
   else:
      print(False)
   