#include "lists.h"

/**
 * check_cycle - check for loop in LL
 * @list: head of linked list
 *
 * Return: 1 if cycled, 0 not cycled
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
	{
		/* No cycle if list is empty or has only one node */
		return (0);
	}

	slow = list;
	fast = list->next;

	while (fast && slow && fast->next)
	{
		if (slow == fast)
		{
			/* cycle detected */
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
