#include <stdio.h>

void troco(int);

int main()
{
    int valor;
    printf("Informe o troco (0 p/ encerrar): ");
    scanf("%d", &valor);
    while (valor != 0) {
        troco(valor);
        printf("\nInforme o troco (0 p/ encerrar): ");
        scanf("%d", &valor);
    }
    return 0;
}


void troco(int valor)
{
    static int notas[8] = { 200, 100, 50, 20, 10, 5, 2, 1 };
    int i, qtde;
    for (i = 0; valor > 0; i++) {
        qtde = valor / notas[i];
        if (qtde > 0) {
            printf("%d notas de R$ %d\n",
                   qtde, notas[i]);
            valor %= notas[i];
        }
    }
}

