'''
Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e depois mostre se ela pode ou não votar.
Autor:Jules do Nascimento Pires
Ex:005
Data:
'''


import os

os.system('cls')

anoNascimento = int(input('Informe o ano de nascimento:'))
anoAtual = int(input('Informe o ano atual:'))

idadePessoa = anoAtual - anoNascimento

print('Sua idade é {} anos'.format(idadePessoa))

if (idadePessoa >= 18):
    print('Você já pode votar!')
else:
    print('Você não pode votar!')