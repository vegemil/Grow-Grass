#include <cstdio>

int main()
{
	int testCase;

	int num1;
	int num2;

	scanf_s("%d", &testCase);

	for (int i = 0; i < testCase; i++)
	{
		scanf_s("%d %d", &num1, &num2);
		printf("%d\n", num1 + num2);
	}

	return 0;
}