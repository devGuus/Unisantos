#ifndef _FILA_H
#define _FILE_H
#include <stdbool.h>

#define QUEUE_MAX 10

typedef int queue_info;

typedef struct {
    queue_info itens[QUEUE_MAX];
    int comeco_, final_, qt_elementos;
} fila_circular;

///Inicializar a Fila
void init_queue(fila_circular* f);
///Inserir na fila
void enqueue(fila_circular* f, queue_info v);
///Remover da fila
queue_info dequeue(fila_circular*f);
///Fila estah cheia?
bool queue_isfull(fila_circular f);
///Fila estah vazia?
bool queue_isempty(fila_circular f);
///Mostra os elementos da fila
int queue_print(fila_circular f);

#endif // _FILA_H
