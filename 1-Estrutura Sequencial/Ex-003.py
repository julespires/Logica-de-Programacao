'''
Faça um programa que receba três notas e seus respectivos pesos, calcule e mostre a média ponderada.
Autor:Jules do Nascimento Pires
Ex:003
Data:01/11/2025
'''

# Utilização da biblioteca de sistema
import os

# Limpa a tela
os.system('cls')

# Entrada das notas e pesos
nota1 = float(input('Primeira nota:'))
peso1 = int(input('Primeiro peso'))
nota2 = float(input('Segunda nota'))
peso2 = int(input('Segundo peso:'))
nota3 = float(input('Terçeira nota:'))
peso3 = int(input('Terçeiro peso:'))

# Calcula a média ponderada
media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3)/(peso1 + peso2 + peso3)

# Mostra a média ponderada
print('Média ponderada das notas:{:.2f}'.format(media))