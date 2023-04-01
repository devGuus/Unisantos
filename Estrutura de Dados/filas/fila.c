#include "fila.h"

///Inicializar a Fila
void init_queue(fila_circular* f){
    f->qt_elementos = f->comeco_ = f->final_ = 0;
    int i;
    for(i = 0; i < QUEUE_MAX; i++){
        f->itens[i] = 0;
    }
}

///Inserir na fila
void enqueue(fila_circular* f, queue_info v) {

    if (queue_isfull(*f))
        return;

    f->itens[f->final_] = v;
    f->final_ = (f->final_ + 1) % QUEUE_MAX;
    f->qt_elementos++;
}
///Remover da fila
queue_info dequeue(fila_circular* f) {
    
    if (queue_isempty(*f))
        // TODO: implementar com valor melhor 
        // para tratar esse tipo de erro
        return 0;

    queue_info v = f->itens[f->comeco_];
    // f->comeco_ = (f->comeco_ + 1) % QUEUE_MAX;
    // Ou:
    if (++(f->comeco_) == QUEUE_MAX)
        f->comeco_ = 0;
    
    f->qt_elementos--;

    return v;
}
///Fila estah cheia?
bool queue_isfull(fila_circular f) {
    return (f.qt_elementos == QUEUE_MAX);
}
///Fila estah vazia?
bool queue_isempty(fila_circular f) {
    return (f.comeco_ == f.final_);
}
