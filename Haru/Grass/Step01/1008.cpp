#include <cstdio>

int main()
{
	int num1 = 0;
	int num2 = 0;

	scanf_s("%d %d", &num1, &num2);

	if (num1 < 0 || num2 > 10)
		return 0;

	printf("%.9f", (double)num1 / num2);

	return 0;
}