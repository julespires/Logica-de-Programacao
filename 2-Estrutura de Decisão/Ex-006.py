'''
Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua média e mostre na tela. No final, 
analise a média e mostre se o aluno teve ou não um bom aproveitamento (se ficou acima da média 7.0).
Autor:Jules do Nascimento Pires
Ex:006
'''

import os

os.system('cls')

nome = str(input('Informe o nome do aluno:'))
nota1 = float(input('Informe a primeira nota:'))
nota2 = float(input('Informe a segunda nota:'))

media = (nota1 + nota2) / 3

print('Média aritimética:{:.2f}'.format(media))

if ( media >= 7.0):
       print('O aluno {} teve um bom aproveitamento!'.format(nome))
else:
       print('O aluno {} tem um mal aproveitamento!'.format(nome))