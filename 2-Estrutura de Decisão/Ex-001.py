'''
Faça um programa que receba quatro notas de um aluno, calcule e mostre a média aritmética das notas e a
mensagem de aprovado ou reprovado, considerando para aprovação média 7.
Autor:Jules do Nascimento Pires
Ex:001
Data:23/10/2025
'''

# Entrada das notas
nota1 = float(input('Primeira nota:'))
nota2 = float(input("Segunda nota:"))
nota3 = float(input("Terçeira nota:"))
nota4 = float(input("Quarta nota:"))

# Calcula a média aritimética
media = (nota1 + nota2 + nota3 ) / 3

# Mostra a média
print("Média aritimética:{:.2f}".format(media))

# Condições
if (media >= 7):
    print('Aluno aprovado"')

else:
    print('Aluno reprovado')