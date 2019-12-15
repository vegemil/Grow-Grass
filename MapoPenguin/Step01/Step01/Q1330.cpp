#define _CRT_SECURE_NO_WARNINGS
#include "Q1330.h"
#include <stdio.h>

using namespace std;

void Q1330() {
	int a, b;

	scanf("%d %d", &a, &b);

	if (a > b)
		printf(">");
	else if (a < b)
		printf("<");
	else
		printf("==");
}
