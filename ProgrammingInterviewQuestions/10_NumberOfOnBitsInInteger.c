#include <stdio.h>
#include <stdlib.h>

#define CHAR_SIZE 8
#define INT_SIZE 32

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

int printIntInBits(unsigned int number) 
{
	int total = 0;
	printf("%x\n", number);

	int mask;
	int i;

	for(i = 0; i < INT_SIZE; i++) {
		if (i % 4 == 0 && i > 0) {
			printf(" ");
		}
		mask = 1 << (INT_SIZE - i - 1);
		int result = mask & number;
		if (result == mask) {
			printf("1");
			total += 1;
		}
		else {
			printf("0");
		}
	}

	printf("\n");
	
	if (total % 2 == 0) {
		printf("EVEN!\n");
		total = 0;
	} else {
		printf("ODD!\n");
		total = 1;
	}

	printf("\n");
	return total;
}

int main(int argc, char **argv) 
{
	if (argc != 2) {
		return EXIT_FAILURE;
	}

	// int size = atoi(argv[2]);
	// int i;

	// printf("\n");

	// for (i = 0; i < size; i++) {
	// 	printCharInBits(argv[1][i]);
	// 	printf(" %x", argv[1][i]);
	// 	printf(" ");
	// }

	//printf("\n");

	//int bits = countOnBits(toCheck);

	//printf("%d\n", bits);

	unsigned int number = atoi(argv[1]);

	printIntInBits(number);

	return EXIT_SUCCESS;
}