#include <stdio.h>
#include <stdlib.h>

typedef struct _node{
	int val;
	struct _node *next;
} node;

node *node_construct(int number) {
	node *new_node = (node *)malloc(sizeof(node));
	new_node->val = number;
	new_node->next = NULL;
	return new_node;
}

void insert_array_into_list(node **list, int *numbers, int length)
{
	node dummy;
	dummy.next = *list;
	node *prev = &dummy;
	node *curr = *list;
	//curr = *list;
	while (curr != NULL) {
		prev = curr;
		curr = curr->next;
	}
	int i;
	for (i = 0; i < length; i++) {
		node *new_node = node_construct(numbers[i]);
		prev->next = new_node;
		prev = new_node->next;
	}

	*list = dummy.next;
	return;
}

void insert_number_into_list(node **list, int number) 
{
	node *new_node = node_construct(number);

	node dummy; 
	dummy.next = *list;
	node *prev = &dummy;
	node *curr = *list;

	prev->next = new_node;
	new_node->next = curr;

	*list = dummy.next;
}

void printList(node *list) {
	if (list == NULL) {
		printf("nothing: NULL\n");
		return;
	}

	node *curr = list->next;
	while (curr != NULL) {
		printf("%d->", curr->val);
		curr = curr->next;
	}
	printf("NULL\n");

	return;
}

int main(int argc, char** argv) 
{
	int numbers[6] = {1, 2, 3, 40, 5, 6};
	int i;
	for (i = 0; i < 6; i++) {
		printf("%d ", numbers[i]);
	}
	printf("\n");

	//node *head = (node *)malloc(sizeof(node));
	head = NULL;

	insert_number_into_list(&head, 6);

	printList(head);

	return EXIT_SUCCESS;
}