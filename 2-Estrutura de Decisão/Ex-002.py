'''
Faça um programa que receba três notas de um aluno, calcule e mostre a média aritmética e a mensagem
constante na tabela a seguir. Aos alunos que ficaram para exame, calcule e mostre a nota que deverão
tirar para serem aprovados, considerando que a média exigida é 6,0.
Autor:Jules do Nascimento Pires
Ex:002
Data:
'''

import os

os.system('cls')

nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
nota3 = float(input('Terçeira nota:'))

media = (nota1 + nota2 + nota3) / 3

print('Média aritimética:{:.2f}'.format(media))

if (media >= 0.0 and media < 3.0):
    print('Reprovado!')

if (media >= 3.0 and media < 7.0):
    print('Fazer exame.')

if (media >= 7.0 and media <= 10.0):
    print("Aprovado!")