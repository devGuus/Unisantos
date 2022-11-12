#include <stdio.h>

int menus(int);

int main(void)
{
    int p, n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        scanf("%d", &p);
        printf("%d\n", menus(p));
    }
    return 0;
}

int menus(int valor)
{
    int cont, qtde, i, precos[] = { 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1 };
    i = cont = 0;
    while(valor > 0){
        qtde = valor / precos[i];
        if(qtde > 0){
            valor %= precos[i];
            cont += qtde;
        }
        i++;
    }
    
    return cont;
}