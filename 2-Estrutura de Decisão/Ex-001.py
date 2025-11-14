'''
Faça um programa que receba dois números informados pelo usuário e mostre o maior.
Autor:Jules do Nascimento Pires
Ex:001
Data:
'''

# Entrada dos valores
num1 = int(input('Primeiro valor:'))
num2 = int(input('Segundo valor:'))

# Condições
if num1 > num2:
    print('O número {} é o maior!'.format(num1))

elif num2 > num1:
    print('O número {} é o maior!'.format(num2))

else:
    print('Os valores são iguais!')