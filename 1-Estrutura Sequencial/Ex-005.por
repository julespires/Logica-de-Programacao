/*
Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.
Autor:Jules do Nascimento Pires
Ex:005
Data:08/10/2025
*/
programa {
  funcao inicio() {
    
    // Guarda o salario e o percentual de aumento
    real salario, percentual
    
    // Entrada do salário e o percentual
    escreva("Informe o salário do funcionário R$:")
    leia(salario)
    escreva("Informe o percentual de aumento R$:")
    leia(percentual)
    
    // Limpa a tela
    limpa()

    // Calcula o salário e o aumento
    real aumento = salario * percentual / 100
    real novoSalario = salario + aumento
    
    // Mostra o valor do aumento e do saláio
    escreva("Valor do aumento R$:" + aumento + "\n")
    escreva("Valor do aumento R$:" + novoSalario)
  }
}
