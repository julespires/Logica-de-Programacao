/*
 Faça um programa que receba o salário base de um funcionário, calcule e mostre seu salário a receber,
sabendo-se que o funcionário tem gratificação de R$ 50 e paga imposto de 10% sobre o salário base.
Autor:Jules do Nascimento Pirees
Ex:007
Data:08/10/2025
*/
programa {
  funcao inicio() {
    
    // Guarda o salário
    real salario
    
    // Entrada do salário
    escreva("Informe o salário: R$")
    leia(salario)
    
    // Limpa a entrada do salário
    limpa()
    
    // Calcula o salário a receber
    real imposto = salario * 10 / 100
    real novoSalario = salario + 50 - imposto
    
    // Mostra o salário a receber
    escreva("Salário a receber: R$" + novoSalario) 
  }
}
