/* Varias Funcões e testes meus em linguagem C */
#include <stdio.h>
#include <math.h>

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
/*
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
}*/

#define MAX 300

typedef struct {
    int peso;
    int valor;
} peso_valor;

peso_valor mochila_rec(int [], int [], int, int, int);
void mochila(int [], int [], int, int);

int main()
{
    int n, pac;
    int peso[MAX], valor[MAX];
    peso_valor result;

    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &pac);
        for (int i = 0; i < pac; i++) {
            scanf("%d %d", &valor[i], &peso[i]);
        }
        //mochila(peso, valor, 50, pac);
        result = mochila_rec(peso, valor, 50, pac, 0);
        printf("%d brinquedos\nPeso: %d kg\n\n", result.valor, result.peso);
    }
    return 0;
}

void mochila(int p[], int v[], int c, int n)
{
    int pos, valor, peso, max_brinq = 0, max_peso, m = (int) pow(2, n);
    for (int i = 0; i < m; i++) {
        valor = peso = 0;
        for (int j = 0; j < n; j++) {
            pos = (i >> j) % 2;
            if (pos == 1) {
                valor += v[j];
                peso += p[j];
            }
        }
        if (peso <= c && valor > max_brinq) {
            max_brinq = valor;
            max_peso = peso;
        }
    }
    printf("%d brinquedos\nPeso: %d kg\n\n", max_brinq, max_peso);
}

peso_valor mochila_rec(int p[], int v[], int c, int n, int item)
{
    peso_valor r = { 0, 0}, r_max, l_max;
    if (c == 0 || item >= n) {
        return r;
    }
    if (p[item] > c) {
        return mochila_rec(p, v, c, n, item + 1);
    }
    r = mochila_rec(p, v, c - p[item], n, item + 1);
    r_max.valor = v[item] + r.valor;
    r_max.peso = p[item] + r.peso;

    l_max = mochila_rec(p, v, c, n, item + 1);
    return (r_max.valor > l_max.valor ? r_max : l_max);
}
