#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - that checks if list is cyclical
 * @list: pointer to list tl check
 * Return: if cyclical 1, otherwise 0.
 */
int check_cycle(listint_t *list)
{
	listin_t *slow = list;
	listin_t *fast = list;

	if (list == NULL)
		return (0);
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
