/*
Sabe-se que:
pé = 12 polegadas
1 jarda = 3 pés
1 milha = 1,760 jarda
Faça um programa que receba uma medida em pés, faça as conversões a seguir e mostre os resultados.
a) polegadas;
b) jardas;
c) milhas.
*/
programa {
  funcao inicio() {
    
    // Guarda a medida em pés
    real pes 
    
    // Recebe a medida pelo usuário
    escreva("Informe uma medida em pés:")
    leia(pes)
    
    // Limpa a tela
    limpa()

    // Realiza a conversão
    real polegadas = pes * 12
    real jardas = pes / 3
    real milhas = jardas / 1760

    // Mostra o resultado da conversão
    escreva("Medida em polegadas " + polegadas + "\n")
    escreva("Medida em jardas " + jardas + "\n")
    escreva("Medida em milhas " + milhas)
  }
}
