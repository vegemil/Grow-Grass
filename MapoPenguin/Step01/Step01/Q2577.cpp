#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string>
#include "Q2577.h"
using namespace std;

void Q2577()
{
	int result[10] = { 0, };
	int A, B, C;

	scanf("%d", &A);
	scanf("%d", &B);
	scanf("%d", &C);

	string mul = to_string(A * B * C);

	for (int i = 0; i < mul.length(); i++)
	{
		int tmp = mul.at(i) - '0';
		result[tmp]++;
	}

	for (int i = 0; i < 10; i++)
		printf("%d\n", result[i]);
}