#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include "Q2588.h"
using namespace std;

void Q2588() {
	int a, b;

	scanf("%d\n%d", &a, &b);

	int ones, tens, hundreds;

	hundreds = b / 100;
	tens = b % 100 / 10;
	ones = b % 10;

	printf("%d\n", a * ones);
	printf("%d\n", a * tens);
	printf("%d\n", a * hundreds);
	printf("%d\n", a * b);
}
