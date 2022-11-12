#include <stdio.h>

typedef struct {
    int hora;
    int min;
} horario;

typedef struct {
    horario inicio;
    horario fim;
} intervalo;

void quicksort(intervalo [], int, int);
int escalonamento(int, intervalo []);
int compara(intervalo, intervalo);
int hora_to_int(horario);

int main()
{
    int n;
    scanf("%d", &n);
    intervalo eventos[n];
    for (int i = 0; i < n; i++) {
        scanf("%d:%d", &eventos[i].inicio.hora, &eventos[i].inicio.min);
        scanf("%d:%d", &eventos[i].fim.hora, &eventos[i].fim.min);
    }
    printf("%d\n", escalonamento(n, eventos));
    return 0;
}

int escalonamento(int n, intervalo evento[])
{
    int i, j = 0, cont = 1;
    quicksort(evento, 0, n - 1);
    for (i = 1; i < n; i++) {
        if (hora_to_int(evento[i].inicio) >= hora_to_int(evento[j].fim)) {
            j = i;
            cont++;
        }
    }
    return cont;
}

int hora_to_int(horario h)
{
    return (h.hora * 100 + h.min); // 7:40 => 7 * 100 + 40 = 740
}

int compara(intervalo a, intervalo b)
{
    if (hora_to_int(a.fim) < hora_to_int(b.fim)) {
        return -1;
    }
    if (hora_to_int(a.fim) == hora_to_int(b.fim)) {
        return hora_to_int(a.inicio) - hora_to_int(b.inicio);
    }
    return 1;
}

void quicksort(intervalo a[], int e, int d) 
{
    int i = e; // índice esquerdo
    int j = d; // índice direito
    intervalo x; // elemento mediano do vetor
    intervalo aux; // variável auxiliar para troca
    x = a[(i+j) / 2];
    do {
        while (compara(a[i], x) < 0) i++;
        while (compara(x, a[j]) < 0) j--;
        if(i <= j) {
            aux = a[i];
            a[i++] = a[j];
            a[j--] = aux;
        }
    } while (i <= j);
    if (e < j) quicksort(a, e, j);
    if (i < d) quicksort(a, i, d);
}
