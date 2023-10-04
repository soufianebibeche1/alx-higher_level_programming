#include "lists.h"


/**
 * insert_node - Inserts a node into a sorted linked list.
 * @head: A pointer to a pointer to the head of the list.
 * @number: The value to be inserted.
 *
 * Return: A pointer to the newly inserted node, or NULL on failure.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *newnode;

	newnode = malloc(sizeof(listint_t));

	if (newnode == NULL)
	{
		return (NULL);
	}

	newnode->n = number;

	if (node == NULL || node->n >= number)
	{
		newnode->next = node;
		*head = newnode;
		return (newnode);
	}

	while (node && node->next && node->next->n < number)
	{
		node = node->next;
	}

	newnode->next = node->next;
	node->next = newnode;

	return (newnode);
}
