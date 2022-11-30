#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node to sorted linked list
 * @head: pointer to pointer to head of teh list
 * @number: number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *ptr1, *ptr2;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	if (new->n < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	ptr1 = *head;
	while (ptr1 != NULL)
	{
		if (new->n < ptr1->n || new->n == ptr1->n)
		{
			new->next = ptr2->next;
			ptr2->next = new;
			return (new);
		}

		ptr2 = ptr1;
		ptr1 = ptr1->next;
	}
	if (new->n > ptr2->n)
	{
		ptr2->next = new;
		new->next = NULL;
	}
	return (new);
}
