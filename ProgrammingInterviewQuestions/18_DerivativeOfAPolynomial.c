#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct {
	int c;
	int power;
} term;

void printEquation(term *eqn, int totalTerms) 
{
	int i;
	for (i = 0; i < totalTerms; i++) {
		fprintf(stdout, "%dx^%d", eqn[i].c, eqn[i].power);
		if (i != totalTerms - 1) {
			fprintf(stdout, "+ ");
		}
	}
	fprintf(stdout, "\n");
}

void derivative(term *eqn, int totalTerms) 
{
	int i;
	for (i = 0; i < totalTerms; i++) {
		eqn[i].c = eqn[i].c * eqn[i].power;
		eqn[i].power--;
	}

	printEquation(eqn, totalTerms);
}

term* initializeEquation(int totalTerms) 
{
	srand(time(NULL));

	term *eqn = (term *)malloc(totalTerms * sizeof(term));

	int i;
	for (i = 0; i < totalTerms; i++) {
		eqn[i].c = rand() % 10 + 10;
		eqn[i].power = i;
	}

	return eqn;
}

int main(int argc, char **argv)
{

	if (argc != 2) {
		return EXIT_FAILURE;
	}
	int totalTerms = atoi(argv[1]);
	term *eqn = initializeEquation(totalTerms);
	printEquation(eqn, totalTerms);
	derivative(eqn, totalTerms);
	return EXIT_SUCCESS;
}