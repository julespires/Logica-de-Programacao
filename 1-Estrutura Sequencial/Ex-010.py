'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Autor:Jules do Nascimento Pires
Ex:010
Data:02/01/2026
'''

import os

os.system('cls')

# Entrada do valor em reais
real = float(input('Quanto dinheiro você tem na carteira?'))

# Realiza a conversão para dolar
dolar = real / 3.27

# Mostra o resultado da conversão
print('Com R${} você pode cmprar U$${:.2f}'.format(real, dolar))