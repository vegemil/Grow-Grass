#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <list>
#include <algorithm>
#include "Q1546.h"
using namespace std;

#define NEW_SCORE(score, M) score/M*100; 

void Q1546()
{
	int count, max;
	list<int> scores;
	double avg = 0;

	scanf("%d", &count);
	scores.resize(count);
	for (int i = 0; i < count; i++)
	{
		int tmp;
		if (i < (count - 1))
			scanf("%d ", &tmp);
		else
			scanf("%d", &tmp);
		
		scores.push_back(tmp);
	}

	max = *max_element(scores.begin(), scores.end());
	
	for (list<int>::iterator it = scores.begin(); it != scores.end(); it++)
	{
		avg += NEW_SCORE(*it, (double)max);
	}

	avg /= count;

	printf("%f", avg);
}