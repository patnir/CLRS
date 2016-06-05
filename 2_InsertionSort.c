#include<stdio.h>
#include<stdlib.h>

void print_array(int *A, int size)
{
	int i;
	for (i = 0; i < size; i++)
	{
		printf("%d ", A[i]);
	}
	printf("\n");
}

void insertion_sort(int *A, int size)
{
	int j;
	for (j = 1; j < size; j++) {
		int key = A[j];
		int i = j - 1;
		while (i >= 0 && A[i] > key) {
			A[i + 1] = A[i];
			i = i - 1;
		}
		A[i + 1] = key;
	}
}


int main(int argc, char **argv)
{
	int A[] = {31, 41, 59, 61, 58};
	print_array(A, 5);
	insertion_sort(A, 5);
	print_array(A, 5);
	return EXIT_SUCCESS;
}
