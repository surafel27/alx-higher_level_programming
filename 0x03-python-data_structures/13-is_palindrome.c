#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - fuction checkes for palindrom
 * listint_t: structure of the list
 * head: stucture of list
 * Return: 0 if it is not palindrom 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *ptr1 = *head;
	int *array;
	int count = 0, i = 0, j;

	while (ptr1 != NULL)
	{
		count++;
		ptr1 = ptr1->next;
	}
	array = malloc(sizeof(int) * count);
	ptr1 = *head;
	while (i < count)
	{
		array[i] = ptr1->n;
		i++;
		ptr1 = ptr1->next;
	}
	i = count - 1;
	for (j = 0; j < (count / 2); j++)
	{
		if (array[j] != array[i])
			return (0);
		i--;
	}
	return (1);
}
