#include <stdio.h>

int main(int argc, char const *argv[])
{
	int valor;
	printf("Informe o troco (0 - finalizar): ");
	scanf("%d", &valor);
	while(valor != 0)
	{
		troco(valor);
		printf("Informe o troco (0 - finalizar): ");
		scanf("%d", &valor);
	}
	return 0;
}

void troco(int valor)
{
	int notas[8] = {200, 100, 50, 20, 10, 5, 1};
	int i, qtd;
	for (int i = 0; valor > 0; ++i)
	{	
		qtd = valor / notas[i];
		if(qtd > 0){
			printf("%d notas de R$ %d\n", qtd, notas[i]);
			valor %= notas[i];
		}
	}
}