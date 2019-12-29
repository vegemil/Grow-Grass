#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include "Q2739.h"
using namespace std;

void Q2739() {
	int a;

	scanf("%d", &a);

	for (int i = 1; i <= 9; i++)
	{
		//2 * 1 = 2
		printf("%d * %d = %d\n", a, i, a * i);
	}
}
