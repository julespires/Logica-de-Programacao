/*
Faça um programa que receba três notas, calcule e mostre a média aritmética.
Autor:Jules do Nascimento Pires
Ex:002
Data:08/
*/
programa {
  // Este programa utiliza a biblioteca Matematica
  inclua biblioteca Matematica --> mat
  funcao inicio() {
    
    // Guarda as notas
    real n1, n2, n3
    
    // Entrada das notas
    escreva("Primeira nota:")
    leia(n1)
    escreva("Segunda nota:")
    leia(n2)
    escreva("Terçeira nota:")
    leia(n3)

    // Calcula a média
    real media = (n1 + n2 + n3) / 3
    
    // Mostra o resultado da média
    escreva("Média aritimética das notas:" + mat.arredondar(media,2))
  }
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 2; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */