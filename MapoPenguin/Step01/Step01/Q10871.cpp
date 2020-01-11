#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include "Q10871.h"
using namespace std;

void Q10871() {
	int count, x;
	int numbers[10000] = { 0 };

	scanf("%d %d", &count, &x);

	for (int i = 0; i < count; i++)
	{
		scanf(" %d", &numbers[i]);
	}

	for (int j = 0; j < count; j++)
	{
		if (numbers[j] < x)
			printf("%d ", numbers[j]);
		else
			continue;
	}
	printf("\n");
}
