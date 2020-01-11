#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include "Q2438.h"
using namespace std;

void Q2438() {
	int stars;

	scanf("%d", &stars);

	for (int i = 1; i <= stars; i++)
	{
		for(int j = 1; j <= i; j++)
			printf("*");
		printf("\n");
	}
}
