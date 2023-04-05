#ifndef _PILHA_H
#define _PILHA_H

#include <stdbool.h>

#define TAMANHO_PILHA 10

typedef int data;

typedef struct {
  data dados[TAMANHO_PILHA];
  int qtd_elementos;
} pilha;

// Inicializando a pilha p no estado vazio
void stack_init(pilha *p);

// devolve verdadeiro se a pilha p estiver vazia e falso, caso contrario
bool stack_isempty(pilha p);

// devolve verdadeiro se a pilha p estiver cheia e falso, caso contrario
bool stack_isfull(pilha p);

// Insere item no topo
void push(pilha *p, data x);

// Insere item no top (teste para rertorna verdadeiro ou falso)
bool push_and_test(pilha *p, data x);

// Remover e devolver item da pilha p
data pop(pilha *p);

// Acessa o ultimo item da pilha p e retorna uma cópia do valor
data top(pilha p);

#endif