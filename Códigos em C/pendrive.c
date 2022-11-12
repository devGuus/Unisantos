#include <stdio.h>
#include <stdlib.h>

int pendrive(int, int, int []);
int compara(const void *, const void *);

int main()
{
    int capacidade, num_arquivos;

    printf("Capacidade do pendrive (MB): ");
    scanf("%d", &capacidade);
    printf("Numero de arquivos: ");
    scanf("%d", &num_arquivos);
    int arquivos[num_arquivos];
    printf("Informe o tamanho de cada arquivo em MB\n");
    for (int i = 0; i < num_arquivos; i++) {
        printf("%do. arquivo: ", i + 1);
        scanf("%d", &arquivos[i]);
    }
    printf("Voce consegue armazena, no maximo, %d arquivos no pendrive\n",
           pendrive(capacidade, num_arquivos, arquivos));
    return 0;
}

int compara(const void * a, const void * b)
{
    int x = *(int *)a;
    int y = *(int *)b;
    return x - y;
}

int pendrive(int capacidade, int num_arquivos, int arquivos[])
{
    int max = 0;
    qsort(arquivos, num_arquivos, sizeof(int), compara);
    for (int i = 0; i < num_arquivos && capacidade >= arquivos[i]; i++) {
        capacidade -= arquivos[i];
        max++;
    }
    return max;
}
