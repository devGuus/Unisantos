#include <stdio.h>

void triplicar(int arr[], int n){
  int i;
  for(i = 0; i < n; ++i){
    printf("%d ", arr[i] * 3);
  }
}

int main(){

  int v[10];
  int t_vetor = 10, i;

  printf("Digite 10 valores para o vetor:\n");
  for(i=0; i < t_vetor; ++i){
    scanf("%d", &v[i]);  
  }
  
  printf("Vetor antes:\n");
  for(i = 0; i < 10; ++i){
    printf("%d ", v[i]);
  }
  
  printf("\nVetor depois:\n");
  triplicar(v, t_vetor);
  return 0;
}
