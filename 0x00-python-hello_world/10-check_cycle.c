#include "lists.h"

/**
 * check_cycle - checks for loops in cycles
 * @list: linked list
 * Return: 0 if there is no loop, or
 * 1 if there is a loop
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr1 = list;
	listint_t *ptr2 = list;

	while (ptr1 != NULL && ptr2 != NULL && ptr2->next != NULL)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;

		if (ptr1 == ptr2)
			return (1);
	}

	return (0);
}
