'''
Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a sua terça parte.
Jules do Nascimento Pires
Ex:008
Data:1/11/2025
'''

# Biblioteca de systema
import os
os.system('cls')

# Entrada do valor
num = float(input('Informe um número:'))

# Calcula o dobro e a terça parte
dobro = num * 2
tercaParte = num / 3

# Mostra o resultado
print('O dobro de {} = {}'.format(num, dobro))
print('A terça parte de {} = {:.5f}'.format(num, tercaParte))