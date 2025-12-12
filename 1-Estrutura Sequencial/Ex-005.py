'''
Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na disciplina.
Autor:Jules do Nascimento Pires
Ex:005
Data:16/11/2025
'''

# Biblioteca de sistema
import os
os.system('cls')

# Entrada das notas
nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))

# Calcula a média aritimética
media = (nota1 + nota2) / 2

# Mostra o resultado
print('Média aritimética {}'.format(media))