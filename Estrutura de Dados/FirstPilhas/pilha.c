#include "pilha.h"

void stack_init(pilha * p){
  p->qtd_elementos = 0;
  for(int i = 0; i < TAMANHO_PILHA; ++i)
    p->dados[i] = 0; // atribuindo zero aos dados
}

//caso a pilha esteje vazia, retorne verdadeiro 
bool stack_isempty(pilha p){
  return (p.qtd_elementos == 0); 
}

//caso a pilha esteje cheia, retorne verdadeiro
bool stack_isfull(pilha p){
  return (p.qtd_elementos == TAMANHO_PILHA); //caso a pilha esteje cheia, retorne verdadeiro
}

// Insere itens no topo da lista
void push(pilha *p, data x){
  p->dados[p->qtd_elementos] = x;
  p->qtd_elementos++;
}

// Teste para inserir itens no topo da lista
bool push_and_test(pilha *p, data x){
  if(stack_isfull(*p))
    return false;
  //caso tenha espaço, insira o item
  push(p, x); 
}

// remove e devolve um item
data pop(pilha* p){
  data x = p->dados[p->qtd_elementos - 1]; //excluindo o valor 
  p->qtd_elementos--; //voltando uma casa

  return x; //retornar o valor excluido
}

// Acessa o ultimo elemento e passa uma copia do valor
data top(pilha p){
  return p.dados[p.qtd_elementos - 1];
}