'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
Autor:Jules do Nascimento Pires
Ex:006
Data:02/01/2026
'''

import os
os.system('cls')

num = int(input('Digite um número:'))

d = num * 2
t = num * 3
r = num **(1/2)

print('O dobro de {} vale {}'.format(num, d))
print('O triplo de {} vale {}'.format(num, t))
print('O raiz quadrada de {} vale {}'.format(num, r))