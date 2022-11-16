/* Varias Funcões e testes meus em linguagem C */
#include <stdio.h>

// While em C
/*
int main()
{
	int contador = 1;
	while(contador <= 5) //Enquanto contador(Variavel) for menor ou igual a 5 faça(continue)
	{
		printf("%d\n", contador);
		contador++; // contador + 1
	}

	return 0;
}
*/
// Aqui fiz uma função recursiva para calcular o fatorial
/*
int main()
{
	int fatorial;

	printf("Digite um valor para ser fatorado: ");
		scanf("%d", &fatorial);

	printf("fatorial de %d e = %d\n",fatorial, ffator(fatorial));

	return 0;
}

ffator(int n){
	int i;

	for(i=1; n>1; n--)
	{
		i = i * n;
	}

	return i;
}*/
/*
printfvetor(int, int[]);

int main()
{

//Escreva uma função recursiva em C para imprimir o conteúdo de um vetor de inteiros.
//A função deve receber como parâmetros o vetor e o tamanho do vetor. O vetor deve ser impresso do primeiro ao último elemento.

	int i, n;

	printf("Digite o tamanho do vetor: ");
		scanf("%d", &n);
	int v[n];
	printf("Digite os valores do vetor: ");

	for(i=0; i<n; i=i+1)
	{
		scanf("%d", &v[i]);
	}
	printfvetor(n, v);
	printf("\n");

    return 0;
}

printfvetor(int n, int v[])
{
	if(n > 0)
	{
		printfvetor(n-1, v);
		printf("%d", v[n-1]);
	}
}*/
int resultado(int);
int main() //Calculando fatorial de forma recursiva
{
    int n;

    printf("Digite um numero para fatorar: ");
        scanf("%d", &n);

    printf("Fatorial de %d = %d", n, fatorial(n));

    return 0;
}

fatorial(int x)
{
    int resultado;

    if(x==0)
    {
        return 1;
    }else{
        resultado = x * fatorial(x - 1); //aqui chamamos a mesma funcao dentro dela, criando dentro do sistema uma segunda funcao para resolver
    }

    return resultado;
}
