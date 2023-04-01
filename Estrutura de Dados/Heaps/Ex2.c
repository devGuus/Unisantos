#include <stdio.h>

void heapfy(int arr[], int n, int i){
  int smallraiz = i;
  int esquerda = 2 * i + 1;
  int direita = 2 * i + 2;

  if(esquerda < n && arr[esquerda] < arr[smallraiz]) //verificando o lado esquerdo
  {
    smallraiz = esquerda;
  }

  if(direita < n && arr[direita] < arr[smallraiz]) //verificando o lado direito
  {
    smallraiz = direita;
  }
  //se a raiz ainda não seja o menor elemento -->
  if(smallraiz != i){
    int aux = arr[i];
    arr[i] = arr[smallraiz];
    arr[smallraiz] = aux;

    heapfy(arr, n, smallraiz);
    
  }
}

void build_minimo(int arr[], int n){
  int i;
  for(i = n / 2 - 1; i >= 0; i--)
    heapfy(arr, n, i);
}

void print_vetor(int arr[], int n){
  int i;
  for(i = 0; i < n; i++){
    printf("%d ", arr[i]);
  }  
  printf("\n");
}

int main(){

  int a[7] = { 10, 4, 6, 1, 5, 8, 3 };
  int b[9] = { 6, 2, 7, 9, 1, 8, 10, 4, 11 };

  int metadeA = sizeof(a) / sizeof(a[7]); //recebendo o vetor em bytes e dividindo
  int metadeB = sizeof(b) / sizeof(b[9]);

  build_minimo(a, metadeA); //chamando a função para contruir a arvore
  build_minimo(b, metadeB);
  
  printf("Heap Mínimo do vetor a: \n");
  print_vetor(a, metadeA); //função que vai printar o vetor
  
  printf("Heap Mínimo do vetor b: \n");
  print_vetor(b, metadeB);

  return 0;
}