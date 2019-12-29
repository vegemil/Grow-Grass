#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include "Q15552.h"
using namespace std;

void Q15552() {
	int caseCount, a, b;

	scanf("%d", &caseCount);

	for (int i = 0; i < caseCount; i++)
	{
		scanf("%d %d", &a, &b);
		printf("%d\n", a + b);
	}
}
