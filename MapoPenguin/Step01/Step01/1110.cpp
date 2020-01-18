#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include "Q1110.h"
using namespace std;

void Q1110()
{
	int a;
	int cycle = 1, newNumber = 0;
	int quotient = 0, remainder = 0;

	scanf("%d", &a);
	newNumber = a;

	while (true)
	{
		if (newNumber >= 10)
			quotient = newNumber / 10;
		else
			quotient = 0;

		remainder = newNumber % 10;

		newNumber = remainder * 10 + ( quotient + remainder ) % 10;

		if (newNumber == a)
			break;
		else
			cycle++;
	}

	printf("%d", cycle);
}
