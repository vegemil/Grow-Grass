#include <cstdio>

int main()
{
	int num;

	scanf_s("%d", &num);

	int sum = 0;

	for (int i = 1; i <= num; i++)
	{
		sum += i;
	}

	printf("%d", sum);

	return 0;
}