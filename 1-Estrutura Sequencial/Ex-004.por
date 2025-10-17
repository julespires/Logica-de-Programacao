/*
Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se
que este sofreu um aumento de 25%.
Autor:Jules do Nascimento Pires
Ex:003
Data:08/10/2025
*/
programa {
  funcao inicio() {
    
    // Guarda o salário
    real salario
    
    // Entrada do salário
    escreva("Informe o seu salário R$:")
    leia(salario)
    
    // Calcula o reajuste
    real aumento = salario * 25 / 100
    real novoSalario = salario + aumento
    
    // Mostra o novo salário com 25 de aumento
    escreva("Seu novo salário com 25% de aumento será: R$" + novoSalario)
  }
}
