#include <stdio.h>

//Atividade realizada por Gustavo Marcos
int main(){

	int n, i, x, saida = 1;
	scanf("%d", &n); //Recebe o tamanho do vetor

	int A[n];

	for(i=0; i<n; i++){
		scanf("%d", &A[i]); //Rebe os valores do vetor
	}

	printf("Digite o numero a ser encontrado: ");
	scanf("%d", &x); //x recebe o valor a ser procurado

	for(i=0; i<n; i++){
		if(x == A[i]){ // se o valor for igual ao que estiver no vetor, então sera escrito na tela
			printf("%d\nQuantidade de saidas: %d", A[i], saida);
			return 0;
		}else{
		    printf("esse valor nao pertence ao vetor, digite novamente:");
            scanf("%d", &x); //coloca um novo valor em x
			saida++; //contador sequencial
		}
	}

	return 0;
}
