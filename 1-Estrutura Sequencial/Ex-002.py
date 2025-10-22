'''
Faça um programa que receba o nome do usuário e dê boas vindas a ele.
Autor:Jules do Nascimento Pires
Ex:002
Data:22/10/2025
'''

import os

os.system('cls')

nome = str(input('Qual é o seu nome?'))

print('Olá {} é um prazer te conhecer!'.format(nome))