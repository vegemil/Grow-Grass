#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <algorithm>
#include "Q10818.h"
using namespace std;

void Q10818()
{
	int count = 0;
	
	//int arr[1000000];
	int m = 1000000, M = -1000000;

	scanf("%d", &count);

	int* numArr = (int*)malloc(sizeof(int) * count);

	for (int i = 0; i < count; i++)
	{
		if (i < (count - 1))
			scanf("%d ", &numArr[i]);
		else
			scanf("%d", &numArr[i]);
	}

	for (int i = 0; i < count; i++)
	{
		m = min(m, numArr[i]);
		M = max(M, numArr[i]);
	}

	printf("%d %d", m, M);

}
