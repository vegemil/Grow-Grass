#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <algorithm>
#include "Q2562.h"
using namespace std;

void Q2562()
{
	int M = -1000000;
	int order = 0;

	int* numArr = (int*)malloc(sizeof(int) * 9);

	for (int i = 0; i < 9; i++)
	{
		scanf("%d", &numArr[i]);
	}

	for (int i = 0; i < 9; i++)
	{
		M = max(M, numArr[i]);
		if (M == numArr[i])
			order = i + 1;
	}

	printf("%d %d", M, order);

}
