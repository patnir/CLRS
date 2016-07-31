#include<stdio.h>
#include<stdlib.h>

typedef struct _node{
	int identity;
	int totalLinks;
	struct _node *link;
} node;

typedef struct _graph {
	node *nodes;
} graph;

node *node_construct(int n)
{
	node *new_node = (node *)malloc(sizeof(node));
	new_node->identity = n;
	new_node->totalLinks = 0;
	return new_node;
}

graph *graph_construct()
{
	graph *new_graph = (graph *)malloc(sizeof(graph));
	int i = 0;
	for (i = 0; i < 200; i++) {
		new_graph->nodes[i] = node_construct(i + 1);
	}
	return new_graph;
}

int main(int argc, char** argv)
{
	graph *graph1 = graph_construct();
	printf("%d\n", (graph1->nodes[1]).identity);
	return EXIT_SUCCESS;
}
