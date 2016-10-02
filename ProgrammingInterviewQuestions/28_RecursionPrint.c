#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
void Seq(int n) {
	assert(n > 0);
	
	if (n == 1) {
		printf("1 ");
		return;
	}
	if (n == 2) {
		printf("1 2 1 ");
		return;
	}

	Seq(n - 2);
	Seq(n - 1);
	printf("%d ", n);
	Seq(n - 1);
	Seq(n - 2);
	return;
}

int main(int argc, char **argv)
{
	if (argc != 2) {
		return EXIT_FAILURE;
	}
	int n = atoi(argv[1]);
	Seq(n);
	printf("\n");
	return EXIT_SUCCESS;
}
