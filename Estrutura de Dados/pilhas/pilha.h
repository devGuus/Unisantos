#ifndef _PILHA_H
#define _PILHA_H

#include <stdbool.h>

#define TAMANHO_PILHA 50

typedef int data;

typedef struct {
    data dados[TAMANHO_PILHA];
    int qt_elementos;
} pilha;

/// inicializa a pilha p no estado vazio
void stack_init(pilha * p);

///devolve verdadeiro se a pilha p estiver vazia e falso, caso contrário
bool stack_isempty(pilha p);
///devolve verdadeiro se a pilha p estiver cheia e falso, caso contrário
bool stack_isfull(pilha p);

///insere o elemento x no topo da pilha p
void push(pilha *p, data x);


///insere o elemento x no topo da pilha p
bool push_and_test(pilha* p, data x);


///remove e devolve o elemento do topo da pilha p
data pop(pilha* p);

//acessa o elemento do topo da pilha p devolvendo uma cópia do seu valor
data top(pilha p);


#endif // _PILHA_H
