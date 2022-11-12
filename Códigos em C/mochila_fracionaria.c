#include <stdio.h>

typedef struct {
    int index;
    float valor;
    float peso;
} item;

void mochila_frac(int, const item[], float, float []);
void quicksort(item[], int, int);
int compara(item, item);

int main()
{
    int n;
    float capacidade;
    printf("Numero de itens: ");
    scanf("%d", &n);
    printf("Capacidade da mochila: ");
    scanf("%f", &capacidade);
    item itens[n];
    float f[n];
    printf("Informe o valor e o peso de cada item:\n");
    for (int i = 0; i < n; i++) {
        scanf("%f %f", &itens[i].valor, &itens[i].peso);
        itens[i].index = i;
    }
    mochila_frac(n, itens, capacidade, f);
    float valor = 0;
    for (int i = 0; i < n; i++) {
        valor += itens[i].valor * f[i];
    }
    printf("Valor maximo da mochila: %.2f\n", valor);
    return 0;
}

int compara(item a, item b)
{
    if (a.valor / a.peso < b.valor / b.peso) {
        return -1;
    }
    if (a.valor / a.peso > b.valor / b.peso) {
        return 1;
    }
    return 0;
}

void quicksort(item a[], int e, int d)
{
    item x, aux;
    int i = e, j = d;
    x = a[(i + j) / 2];
    do {
        while (compara(a[i], x) > 0) i++;
        while (compara(a[j], x) < 0) j--;
        if (i <= j) {
            aux = a[i];
            a[i++] = a[j];
            a[j--] = aux;
        }
    } while (i <= j);
    if (j > e) quicksort(a, e, j);
    if (i < d) quicksort(a, i, d);
}

void mochila_frac(int n, const item itens[], float c, float f[])
{
    item aux[n];
    int i;
    for (i = 0; i < n; i++) {
        aux[i] = itens[i];
        f[i] = 0;
    }
    quicksort(aux, 0, n - 1);
    for (i = 0; i < n && aux[i].peso <= c; i++) {
        f[aux[i].index] = 1;
        c -= aux[i].peso;
    }
    if (i < n) {
        f[aux[i].index] = c / aux[i].peso;
    }
}
