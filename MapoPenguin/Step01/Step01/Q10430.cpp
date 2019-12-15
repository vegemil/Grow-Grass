//첫째 줄에(A + B) % C, 둘째 줄에(A% C + B % C) % C, 셋째 줄에(A×B) % C, 넷째 줄에(A% C × B% C) % C를 출력한다.

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
