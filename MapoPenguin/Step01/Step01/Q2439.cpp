#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include "Q2439.h"
using namespace std;

void Q2439() {
	int stars;

	scanf("%d", &stars);

	for (int i = 1; i <= stars; i++)
	{
		for (int j = 1; j <= stars; j++)
		{
			if (j > stars - i)
				printf("*");
			else
				printf(" ");
		}
		printf("\n");
	}
}
