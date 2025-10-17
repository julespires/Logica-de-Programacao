/*
Faça um programa que receba o salário base de um funcionário, calcule e mostre o salário a receber,
sabendo-se que o funcionário tem gratificação de 5% sobre o salário base e paga imposto de 7% tam-
bém sobre o salário base.
Autor:Jules do Nascimento Pires
Ex:006
Data:08/10/2025
*/
programa {
  funcao inicio() {
    
    // Guarda o salário
    real salario
    
    //Entrada do salário
    escreva("Informe o salário base R$:")
    leia(salario)
    
    // Calculos
    real gratificacao = salario * 5 / 100
    real imposto = salario * 7 / 100
    real novoSalario = salario + gratificacao - imposto
    
    // Mostra o novo salário
    escreva("Salário a receber R$" + novoSalario)
  }
}
