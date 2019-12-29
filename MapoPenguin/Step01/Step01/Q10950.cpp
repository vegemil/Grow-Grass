#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include "Q10950.h"
using namespace std;

void Q10950() {
	int caseCount, a, b;

	scanf("%d", &caseCount);

	for (int i = 0; i < caseCount; i++)
	{
		scanf("%d %d", &a, &b);
		printf("%d\n",a + b);
	}
}
