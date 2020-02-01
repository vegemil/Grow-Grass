#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string>
#include "Q8958.h"
using namespace std;

void Q8958()
{
	int count;
	int totalScore = 0, accScore = 0;

	scanf("%d", &count);
	for (int i = 0; i < count; i++)
	{
		char mul[80] = {};
		scanf("%s", &mul);
		totalScore = 0;
		accScore = 0;
		for (int j = 0; j < 80; j++)
		{
			if (mul[j] == 'O')
			{
				accScore++;
				totalScore += accScore;
			}
			else
			{
				accScore = 0;
			}
		}
		printf("%d\n", totalScore);
	}
}