#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include "Q10817.h"

void Q10817()
{
	int a, b, c;

	scanf("%d %d %d", &a, &b, &c);

	if (a > b)
	{
		if (a > c)
		{
			if (b > c)
				printf("%d", b);
			else
				printf("%d", c);
		}
		else
			printf("%d", a);
	}
	else
	{
		if (a > c)
			printf("%d", a);
		else
		{
			if (b > c)
				printf("%d", c);
			else
				printf("%d", b);
		}
	}
}