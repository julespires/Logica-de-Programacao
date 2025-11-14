'''
Faça um programa que receba três notas de um aluno, calcule e mostre a média aritmética das notas e a
mensagem de aprovado ou reprovado, considerando para aprovação média 7.
Autor:Jules do Nascimento Pires
Ex:002
Data:
'''

# Entrada das notas
nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
nota3 = float(input('Terçeira nota:'))

# Média
media = (nota1 + nota2 + nota3) / 3

# Resultado
print('Média aritimética:{:.2f}'.format(media))

# Condições
if (media >= 7):
    print('Aprovado!')

else:
    print('Reprovado!')