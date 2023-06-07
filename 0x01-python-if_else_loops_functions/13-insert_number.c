#include "lists.h"

/**
 * insert_node - inserts a number in a linked list in sorted order
 * @head: pointer to the head node
 * @number: the number to be inserted
 *
 * Return: the address of the new node or NULL (Failure)
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *newNode;

	temp = *head;
	newNode = (listint_t *)malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	while (temp->next != NULL && temp->next->n < number)
	{
		temp = temp->next;
	}

	newNode->next = temp->next;
	temp->next = newNode;

	return (newNode);
}
