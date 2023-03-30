#include <stdio.h>

void heap(int arr[], int n, int i) {
  int maior_el = i;
  int l = 2 * i + 1;
  int r = 2 * i + 2;

  if (l < n && arr[l] > arr[maior_el])
    maior_el = l;

  if (r < n && arr[r] > arr[maior_el])
    maior_el = r;

  if (maior_el != i) {
    int temp = arr[i];
    arr[i] = arr[maior_el];
    arr[maior_el] = temp;

    heap(arr, n, maior_el);
  }
}

void build_heap(int arr[], int n) {
  for (int i = n / 2 - 1; i >= 0; i--)
    heap(arr, n, i);
}

void print_array(int arr[], int n) {
  for (int i = 0; i < n; ++i)
    printf("%d ", arr[i]);
  printf("\n");
}

int main() {
  int a[] = {10, 4, 6, 1, 5, 8, 3};
  int n_a = sizeof(a) / sizeof(a[0]);

  build_heap(a, n_a);

  printf("Vetor a (heap máximo):\n");
  print_array(a, n_a);

  return 0;
}