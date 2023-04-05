#include <stdio.h>
#include "pilha.h"

int main() {

  int vl_inserir;
  pilha p;
  
  stack_init(&p); // iniciamos a função

  // printando se esta vazio ou cheio
  printf("Verificando arquivo...\n");
  if(stack_isempty(p)){
    printf("O arquivo está vazio!\n");
  }else {
    printf("O arquivo está cheio!\n");
  }

  printf("Digite um valor para ser inserido:\n");
    scanf("%d", &vl_inserir);
  push(&p, vl_inserir);

  printf("Imprimindo uma cópia do topo da pilha: %d", top(p));
  
  printf("\nFunção pop();\nValor removido: %d\n", pop(&p));

  return 0;
}