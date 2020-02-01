#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <list>
#include "Q3052.h"
using namespace std;

void Q3052()
{
	list<int> remainders[10];
	
	int tmp;
	for (int i = 0; i < 10; i++)
	{
		scanf("%d", &tmp);
		remainders->push_back(tmp % 42);
	}

	remainders->sort();
	remainders->unique();

	printf("%d", remainders->size());
}