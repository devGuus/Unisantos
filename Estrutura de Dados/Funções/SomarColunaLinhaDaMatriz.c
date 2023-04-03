#include <stdio.h>
#include <stdlib.h>
#include <math.h>
//Função de somar linhas de uma matriz
int somador(int m[][5], int linha){
  int i, soma = 0;
  for(i=0; i < 5; ++i)
    soma += m[linha][i];
  return soma;
}
//Função de somar colunas de uma matriz
int somadorColuna(int m[][5], int coluna){
  int i, soma = 0;
  for(i=0; i<5; ++i)
    soma += m[i][coluna];
  return soma;
}

//imprime a matriz
void print(int m[][5], int tam){
  int j, i;
    for(i=0; i < tam; ++i){
      for(j=0; j < tam; ++j){
        printf("%2d ", m[i][j]);
      }
      printf("\n");
    }
}

int main(){

  int m[5][5];
  int i, j, tam=5;

  srand(time(NULL)); //Não vai gerar numeros aleatorios toda vez
  
  for(i=0; i < tam; ++i){
    for(j=0; j < tam; ++j){
      m[i][j] = rand() % 100;
    }
  }
  print(m, tam);
  printf("\n");
  for(i = 0; i < tam; ++i)
    printf("Soma da linha %d: %d\n", i, somador(m, i));
  printf("\n \n");
  for(i = 0; i < tam; ++i)
    printf("Soma da coluna %d: %d\n", i, somadorColuna(m, i));
  
  return 0;
}