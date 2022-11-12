#include <stdio.h>
#include <math.h>

typedef struct {
    int index;
    int peso;
    int valor;
} item;

void mochila_frac(int, const item [], int, double []);
void quicksort(item [], int, int);

int main()
{
    int t, n, c;
    item itens[1000];
    double f[1000];
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        scanf("%d %d", &n, &c);
        for (int j = 0; j < n; j++) {
            scanf("%d", &itens[j].peso);
            itens[j].index = j;
        }
        for (int j = 0; j < n; j++) {
            scanf("%d", &itens[j].valor);
        }
        mochila_frac(n, itens, c, f);
        double valor_machila = 0;
        for (int j = 0; j < n; j++) {
            valor_machila += f[j] * itens[j].valor;
        }
        printf("%.0lf\n", valor_machila);
    }
    return 0;
}


void mochila_frac(int n, const item itens[], int c, double f[])
{
    item aux[n];
    for (int i = 0; i < n; i++) {
        aux[i] = itens[i];
        f[i] = 0.0;
    }
    quicksort(aux, 0, n - 1);
    int i = 0;
    while (i < n && c >= aux[i].peso) {
        f[aux[i].index] = 1;
        c -= aux[i].peso;
        i++;
    }
    if (i < n) {
        f[aux[i].index] = (double) c / aux[i].peso;
    }
}

void quicksort(item a[], int e, int d) 
{
    int i = e; // índice esquerdo
    int j = d; // índice direito
    item x; // elemento mediano do vetor
    item aux; // variável auxiliar para troca
    x = a[(i+j) / 2];
    do {
        while ((double) a[i].valor/a[i].peso > (double) x.valor/x.peso) i++;
        while ((double) x.valor/x.peso > (double) a[j].valor/a[j].peso) j--;
        if(i <= j) {
            aux = a[i];
            a[i++] = a[j];
            a[j--] = aux;
        }
    } while (i <= j);
    if (e < j) quicksort(a, e, j);
    if (i < d) quicksort(a, i, d);
}