/*
Faça um programa que receba quatro notas de um aluno, calcule e mostre a média aritmética das notas e a
mensagem de aprovado ou reprovado, considerando para aprovação média 7.
*/
programa {
  funcao inicio() {
    
    real nota1, nota2, nota3, nota4

    escreva("Primeira nota:")
    leia(nota1)
    escreva("Segunda nota:")
    leia(nota2)
    escreva("Terçeira nota:")
    leia(nota3)
    escreva("Quarta nota:")
    leia(nota4)

    real media = (nota1 + nota2 + nota3 + nota4) / 4
    
    se (media >= 7.0){
      escreva("Ano aprovado!")
    }senao{
      escreva("Aluno reprovado!")
    }
      escreva("Média aritimética das notas:" + media)
  }
}
