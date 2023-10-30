#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - that checks if list is cyclical
 * @list: pointer to list tl check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listin_t *s = list;
	listin_t *f = list;

	while (f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}
	return (0);
}
