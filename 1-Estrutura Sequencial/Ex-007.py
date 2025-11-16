'''
Faça um programa que leia um número inteiro e mostre o seu antecessor e seu sucessor.
Autor:Jules do Nascimento Pires
Ex:007
Data:16/11/2025
'''

# Biblioteca de sistema
import os

# Limpa a tela
os.system('cls')

num = int(input('Digite um número:'))

print('O antecesor de {} = {}'.format(num, num - 1))
print('O sucessor {} = {}'.format(num, num + 1))