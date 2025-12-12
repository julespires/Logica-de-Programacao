'''
Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80Km/h, exiba uma mensagem dizendo que o usuário
foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.
Autor:Jules do Nascimento Pires
Ex:004
Data:
'''

# Recebe a velocidade
velocidade = float(input('Informe a velocidade do carro:'))

# Condições
if velocidade > 80:
    print('Você foi multado, valor da multa:R${}'.format(velocidade * 5))
    
else:
    print('Velocidade permitida!')