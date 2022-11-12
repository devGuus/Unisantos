#include <stdio.h>

void quicksort(int [], int, int);

int main()
{
    static int a[200000];
    int t, n, x, eat, dif, last_type;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        scanf("%d %d", &n, &x);
        for (int j = 0; j < n; j++) {
            scanf("%d", &a[j]);
        }
        quicksort(a, 0, n - 1);
        eat = n - x;
        dif = 0;
        last_type = -1;
        for (int j = 0; j < n && eat > 0; j++) {
            if (a[j] != last_type) {
                dif++;
                last_type = a[j];
                eat--;
            }
        }
        printf("%d\n", dif);
    }
    return 0;
}

void quicksort(int a[], int e, int d) 
{
    int i = e; // índice esquerdo
    int j = d; // índice direito
    int x; // elemento mediano do vetor
    int aux; // variável auxiliar para troca
    x = a[(i+j) / 2];
    do {
        while (a[i] < x) i++;
        while (x < a[j]) j--;
        if(i <= j) {
            aux = a[i];
            a[i++] = a[j];
            a[j--] = aux;
        }
    } while (i <= j);
    if (e < j) quicksort(a, e, j);
    if (i < d) quicksort(a, i, d);
}