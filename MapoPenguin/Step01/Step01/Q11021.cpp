#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include "Q11021.h"
using namespace std;

void Q11021() {
	int caseCount, a, b;

	scanf("%d", &caseCount);

	for (int i = 1; i <= caseCount; i++)
	{
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d\n", i, a + b);
	}
}
