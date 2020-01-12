#include <cstdio>

int main()
{
	int num1, num2;

	while (scanf_s("%d %d", &num1, &num2) != EOF)
	{
		if ((num1 == 0) && (num2 == 0))
			break;
		else
			printf("%d\n", num1 + num2);
	}

	return 0;
}