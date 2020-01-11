#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include "Q10952.h"
using namespace std;

void Q10952()
{
	int a, b;
	while (true)
	{
		scanf("%d %d", &a, &b);

		if (a + b == 0)
			break;

		printf("%d\n", a + b);
	}
}
