#include <cstdio>

int main()
{
	int num1 = 0;
	int num2 = 0;

	scanf_s("%d %d", &num1, &num2);

	printf("%d\n", num1 + num2);
	printf("%d\n", num1 - num2);
	printf("%d\n", num1 * num2);
	printf("%d\n", num1 / num2);
	printf("%d", num1 % num2);

	return 0;
}