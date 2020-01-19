#include <cstdio>

int main()
{
	int num1, num2, num3;
	int finalNum;
	int ary[10] = { 0 };
	
	scanf_s("%d %d %d", &num1, &num2, & num3);
	finalNum = num1 * num2 * num3;

	while(finalNum != 0)
	{
		ary[finalNum % 10] += 1;
		finalNum /= 10;
	}

	for (int i = 0; i < 10; i++)
	{
		printf("%d\n", ary[i]);
	}
}