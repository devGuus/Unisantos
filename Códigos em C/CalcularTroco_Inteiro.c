#include <stdio.h>

int main(int argc, char const *argv[])
{
	int notas[] = {200, 100, 50, 20, 10, 5, 2, 1};
	int i, qtd, valor, valor_cliente, resto;
    int close;
    close=1;
    while(close != 0)
    {
        printf("Total da compra:");
            scanf("%d", &valor);
		printf("Valor pago pelo cliente:");
            scanf("%d", &valor_cliente);
            resto = (valor_cliente - valor);
            printf("Valor de troco: R$ %d\n", resto);

        for(i=0; i < 8; i++)
        {
            qtd = resto / notas[i];
            if (qtd > 0)
            {
                printf("%d notas de R$ %d\n", qtd, notas[i]);
                resto %= notas[i];
                if(resto == 0)
                {
                    break;
                }
            }
        }
        printf("Deseja continuar? (0/Fechar) ou (1/Continuar)\n");
            scanf("%d", &close);
    }

    printf("\n@GuusDeveloper!");

	return 0;
}
