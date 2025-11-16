'''
Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR.
Autor:Jules do Nascimento Pires
Ex:007
'''

import os

os.system('cls')

num = int(input('Digite um valor:'))

if (num % 2 == 0):
    print('O número {} é par!'.format(num))

else:
    print('O número {} é impar!'.format(num))