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
	return (int)((left + right) / 2.0);
}

void quickSort(int *A, int left, int right, int length)
{
	if (left >= right) {
		return;
	}
	int i = left + 1;
	int j = left + 1;
	int pivot = choosePivot(A, left, right);
	swap(A, pivot, left);
	while (j <= right) {
		if (A[j] < A[left]) {
			swap(A, i, j);
			i += 1;
		}
		j += 1;
	}
	swap(A, left, i - 1);
	printArray(A, length);
	quickSort(A, left, i - 2, length);
	quickSort(A, i, right, length);
}

int main(int argc, char **argv)
{
	if (argc != 2) {
		fprintf(stderr, "Enter length of array.\n");
		return EXIT_FAILURE;
	}
	int length = atoi(argv[1]);

	int *A = (int*)malloc(length * sizeof(int));
	
	if (A == NULL) {
		return EXIT_FAILURE;
	}

	randomInitialization(A, length);
	printArray(A, length);
	quickSort(A, 0, length - 1, length);
	printArray(A, length);
	free(A);
	return EXIT_SUCCESS;
}
