#include <stdio.h>
#include <stdlib.h>

#define CHAR_SIZE 8

void printCharInBits(unsigned char check) 
{
	int mask;
	int result;
	int i;

	for (i = 0; i < CHAR_SIZE; i++) {
		mask = 1 << (CHAR_SIZE - i - 1);
		result = mask & check;
		if (result == mask) {
			printf("1");
		}
		else {
			printf("0");
		}
	}
}

int countOnBits(unsigned int check) 
{
	int total = 0;
	printf("%x\n", check);
	return total;
}

int main(int argc, char **argv) 
{
	if (argc != 3) {
		return EXIT_FAILURE;
	}

	int size = atoi(argv[2]);
	int i;

	printf("\n");

	for (i = 0; i < size; i++) {
		printCharInBits(argv[1][i]);
		printf(" %x", argv[1][i]);
		printf(" ");
	}

	printf("\n");

	//int bits = countOnBits(toCheck);

	//printf("%d\n", bits);

	return EXIT_SUCCESS;
}