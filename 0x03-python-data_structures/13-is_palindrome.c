#include "lists.h"

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Double pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
*/

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev_slow = NULL;
	listint_t *second_half = NULL, *stack = NULL, *temp, *first_half = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}
	prev_slow->next = NULL;

	while (slow != NULL)
	{
		temp = slow->next;
		slow->next = stack;
		stack = slow;
		slow = temp;
	}
	while (first_half != NULL && stack != NULL)
	{
		if (first_half->n != stack->n)
			return (0);
		first_half = first_half->next;
		stack = stack->next;
	}

	return (1);
}
