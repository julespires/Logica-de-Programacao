'''
Faça um programa que receba duas notas, calcule e mostre a média aritmética e a mensagem que se encontra
na tabela a seguir:
Autor:Jules do Nascimento Pires
Ex:003
Data:
'''

# Entrada das notas
nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))

# Calcula a média
media = (nota1 + nota2) / 2

# Mostra a média
print('Média aritimética:{}'.format(media))

# Condicionais
if (media >= 0 and media < 3):
    print('Aluno reprovado')

elif (media >= 3 and media < 7):
    print('Fazer exame!')

elif (media >= 7 and media <= 10):
    print('Aluno aprovado!')
