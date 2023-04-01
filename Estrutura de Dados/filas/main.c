#include <stdio.h>
#include "fila.h"


int main()
{

	fila_circular f;

	init_queue(&f);

	enqueue(&f, 23);
	enqueue(&f, 5);
	enqueue(&f, 10);
	printf("%d", dequeue(&f));
	enqueue(&f, 13);
	enqueue(&f, 22);
	enqueue(&f, 17);
	enqueue(&f, 16);
	enqueue(&f, 44);
	int i;
	for (i = 0; i <= QUEUE_MAX - f.qt_elementos + 1; i++) {
		enqueue(&f, i * 100);
	}


	return 0;

}
