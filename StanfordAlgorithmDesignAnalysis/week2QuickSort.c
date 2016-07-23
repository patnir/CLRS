#include<stdio.h>
#include<stdlib.h>

void printArray(int *A, int length) 
{
	int i;
	for (i = 0; i < length; i++) {
		fprintf(stdout, "%d ", A[i]);
	}	
	fprintf(stdout, "\n");
}

void randomInitialization(int *A, int length) 
{
	int i;
	for (i = 0; i < length; i++) { 
		A[i] = rand() % 10;
	}
}

void swap(int *A, int a, int b) 
{
	int temp = A[a];
	A[a] = A[b];
	A[b] = temp;
}

int choosePivot(int *A, int left, int right) 
{
	return (int) ((left + right) / 2);
}

int main(int argc, char **argv)
{
	int length = 8;
	int *A = (int*)malloc(length * sizeof(int));
	
	if (A == NULL) {
		return EXIT_FAILURE;
	}

	randomInitialization(A, length);
	printArray(A, 8);
	free(A);
	return EXIT_SUCCESS;
}
