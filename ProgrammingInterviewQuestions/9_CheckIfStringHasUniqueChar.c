#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int isUnique(char *word, int length) 
{
	int i;
	int j;
	for (i = 0; i < length; i++) {
		for (j = i + 1; j < length; j++) {
			if (word[i] == word[j]) {
				printf("Not Unique! %c\n", word[i]);
				return 0;
			}
		}
	}
	printf("Unique!\n");
	return 1;
}

void swap(char *word, int a, int b) 
{
	char temp = word[a];
	word[a] = word[b];
	word[b] = temp;
}

void merge(char *word, int s, int m, int e) 
{
	if (e - s == 1) {
		if (word[s] > word[e]) {
			swap(word, s, e);
		}
		return;
	}

	int length1 = m - s + 1;
	int length2 = e - m;
	char *array1 = (char *)malloc(sizeof(char) * length1);
	char *array2 = (char *)malloc(sizeof(char) * length2);

	int k = 0;
	int j = 0;

	int i;

	for (i = s; i <= e; i ++) {
		if (i <= m) {
			array1[k++] = word[i];
		}
		else {
			array2[j++] = word[i];
		}
	}

	k = 0; 
	j = 0;

	for (i = s; i <= e; i++) {
		if ((k < length1 && array1[k] < array2[j]) || j >= length2) {
			word[i] = array1[k++];
		} 
		else {
			word[i] = array2[j++];
		}
	}

	free(array1);
	free(array2);

	return;
}

void mergeSort(char *word, int start, int end) 
{
	if (start >= end) {
		return;
	}

	int mid = (end + start) / 2;
	mergeSort(word, start, mid);
	mergeSort(word, mid + 1, end);
	merge(word, start, mid, end);

	return;
}

int main(int argc, char **argv) 
{
	if (argc == 1) {
		printf("Error!\n\n");
		return EXIT_FAILURE;
	}

	int length = strlen(argv[1]);
	int total = isUnique(argv[1], length);
	printf("Result = %d\n", total);

	mergeSort(argv[1], 0, length - 1);

	//swap(argv[1], 0, 1);
	printf("%s\n", argv[1]);
	return EXIT_SUCCESS;
}
