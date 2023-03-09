#include "pilha.h"

/// inicializa a pilha p no estado vazio
void stack_init(pilha * p){
    p->qt_elementos = 0;
    int i;
    for(i = 0; i < TAMANHO_PILHA; i++){
        p->dados[i] = 0;
    }
}

///devolve verdadeiro se a pilha p estiver vazia e falso, caso contrário
bool stack_isempty(pilha p) {
    return (p.qt_elementos == 0);
}
///devolve verdadeiro se a pilha p estiver cheia e falso, caso contrário
bool stack_isfull(pilha p) {
    return (p.qt_elementos == TAMANHO_PILHA);
}

///insere o elemento x no topo da pilha p
void push(pilha* p, data x) {
    p->dados[p->qt_elementos] = x;
    p->qt_elementos++;
}

bool push_and_test(pilha* p, data x) {
    if (stack_isfull(*p))
        return false;
    
    push(p, x);
}


///remove e devolve o elemento do topo da pilha p
data pop(pilha* p) {
    data x = p->dados[p->qt_elementos - 1];
    p->qt_elementos--;

    return x;
}

data top(pilha p) {
    //if(stack_isempty(p))
    return p.dados[p.qt_elementos - 1];
}