#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include "Q2884.h"

void Q2884()
{
	int hour, min;

	scanf("%d %d", &hour, &min);

	min -= 45;

	if (min < 0)
	{
		hour--;
		if (hour < 0)
			hour = 23;

		min += 60;
	}

	printf("%d %d", hour, min);
}