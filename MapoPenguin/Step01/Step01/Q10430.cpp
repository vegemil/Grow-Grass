//ù° �ٿ�(A + B) % C, ��° �ٿ�(A% C + B % C) % C, ��° �ٿ�(A��B) % C, ��° �ٿ�(A% C �� B% C) % C�� ����Ѵ�.

#define _CRT_SECURE_NO_WARNINGS
#include "Q10430.h"
#include <stdio.h>

using namespace std;

void Q10430()
{
	int a, b, c;

	scanf("%d %d %d", &a, &b, &c);

	printf("%d\n", (a + b) % c);
	printf("%d\n", (a % c + b % c) % c);
	printf("%d\n", (a * b) % c);
	printf("%d\n", (a % c * b % c) % c);
}
