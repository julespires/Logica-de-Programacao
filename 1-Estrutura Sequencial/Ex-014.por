/*
Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
a) a idade dessa pessoa;
b) quantos anos ela terá em 2050.
Autor:Jules do Nascimento Pires
Ex:014
*/
programa {

  inclua biblioteca Calendario --> cal
  funcao inicio() {
    
    // Guarda o ano de nascimento
    inteiro anoNasc
   
    // Recebe  o ano pelo usuário
    escreva("Informe o ano de nascimento:")
    leia(anoNasc)
    
    // Calcula a idade atual e em 2050
    inteiro idadePessoa = cal.ano_atual() - anoNasc
    inteiro idade2050 = 2050 - anoNasc 
    
    // Mostra a idade atual e em 2050
    escreva("Idade atual " + idadePessoa + " anos" + " \n")
    escreva("Idade em 2050 " + idade2050 + " anos")
  }
}
