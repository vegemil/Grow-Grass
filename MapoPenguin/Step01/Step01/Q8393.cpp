#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include "Q8393.h"
using namespace std;

void Q8393()
{
	int inp;
	int sum = 0;

	scanf("%d", &inp);

	for (int i = 1; i <= inp; i++)
	{
		sum += i;
	}

	printf("%d", sum);
}
