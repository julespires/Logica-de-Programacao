'''
Desenvolva um algoritmo que leia dois números inteiros e mostre o somatório
entre eles.
Ex:
Digite um valor: 8
Digite outro valor: 5
A soma entre 8 e 5 é igual a 13.
Autor:Jules do Nascimento Pires
Ex:004
Data:01/01/2026
'''

# Entrada dos números
num1 = int(input('Primeiro valor:'))
num2 = int(input('Segundo valor:'))

# Realiza a soma
soma = num1 + num2

# Mostra o resultado
print('A soma entre {} + {} = {}'.format(num1,num2,soma))