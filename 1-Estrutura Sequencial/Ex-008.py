'''
Faça um programa que receba dois números, calcule e mostre a divisão do primeiro número pelo
segundo. Sabe-se que o segundo número não pode ser zero, portanto, não é necessário se preocupar
com validações.
Autor:Jules do Nascimento Pires
Ex:008
'''

# Entrada dos números
num1 = int(input("Primeiro valor:"))
num2 = int(input("Segundo valor:"))

# Calculo da divisão
divisao = num1 / num2

# Mostra o resultado
print("A divisão de {} / {} = {}".format(num1, num2, divisao))