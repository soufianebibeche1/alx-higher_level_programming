#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Check if a singly linked list has a cycle.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *head1 = list, *head2 = list;

	while (head2 != NULL && head2->next != NULL)
	{
		head1 = head1->next;
		head2 = head2->next->next;

		if (head1 == head2)
		{
			return (1);
		}
	}

	return (0);
}
