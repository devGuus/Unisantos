#include <stdio.h>
#include "pilha.h"

#define NOME_ARQUIVO "C:/Users/CEITELABINFO/Desktop/main.c"

int is_abertura(char c) {
    char charac[] = { '(','[','{' };
    int i;
    for (i = 0; i < sizeof(charac) / sizeof(charac[0]); i++){
        if (c == charac[i])
            return i;
    }

    return -1;
}

int is_fechamento(char c) {
    char charac[] = { ')',']','}' };
    int i;
    for (i = 0; i < sizeof(charac) / sizeof(charac[0]); i++) {
        if (c == charac[i])
            return i;
    }

    return -1;
}


bool is_num(char c) {
    return (c >= '0' && c <= '9');
}

int faz_operacao(data n1, data n2, char op) {
    switch (op) {
    case '+': return n1 + n2;
    case '-': return n1 - n2;
    case '*': return n1 * n2;
    case '/': return n1 / n2;
    }
}

int main()
{

    const char* exp = "73+64-/9*";

    pilha p;

    stack_init(&p);

    char c;
    int i;

    for(i = 0; i < exp[i] != '\0'; i++){
        if (is_num(exp[i])) {
            push(&p, exp[i]-'0');
        } else {
            data num2 = pop(&p);
            data num1 = pop(&p);
            data res = faz_operacao(num1, num2, exp[i]);
            push(&p, res);
        }
    }

    printf("%d", top(p));





    stack_init(&p);
    
    /*Lê o arquivo*/
    FILE* f = fopen(NOME_ARQUIVO, "r");
    
    

    int linha, caracter;
    caracter = linha = 1;

    while ((c = fgetc(f)) != EOF){
        int index;
        if (c == '\n') {
            linha++;
            caracter = 1;
        } else {
            caracter++;
        }
        if ((index = is_abertura(c)) != -1) {
            push(&p, index);
        } else if ( (index = is_fechamento(c)) != -1) {
            if (index == top(p)) {
                pop(&p);
            } else {
                printf("Erro!!! caracter %d, linha %d\n", caracter, linha);
            }
        }
    }

    printf("\n");

    /*Verifica se a pilha tá vazia*/
    if (stack_isempty(p)) {
        printf("Arquivo ok!");
    } else {
        printf("Arquivo com erro!");
    }

    return 0;
}
