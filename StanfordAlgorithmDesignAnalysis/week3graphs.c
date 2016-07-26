#include<stdio.h>
#include<stdlib.h>

typedef struct _node{
	int n;
	struct _node *link;
} node;


node *node_construct(int n)
{
	node *new_node = (node *)malloc(sizeof(node));
	new_node->n = n;
	return new_node;
}

int main(int argc, char** argv)
{
	node *firstNode = NULL;
	firstNode = node_construct(5);
	printf("firstNode->n = %d\n", firstNode->n);
	return EXIT_SUCCESS;
}
