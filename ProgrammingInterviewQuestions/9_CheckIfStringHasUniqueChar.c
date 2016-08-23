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

int main(int argc, char **argv) 
{
	if (argc == 1) {
		printf("Error!\n\n");
		return EXIT_FAILURE;
	}

	int length = strlen(argv[1]);
	int total = isUnique(argv[1], length);
	printf("Result = %d\n", total);
	return EXIT_SUCCESS;
}
