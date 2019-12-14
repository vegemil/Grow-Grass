#include <cstdio>

int main()
{
	int num1 = 0;
	int num2 = 0;
	int num3 = 0;
	int num4 = 0;
	int num5 = 0;

	scanf_s("%d %d", &num1, &num2);

	num3 = num1 * (num2 % 10);
	printf("%d\n", num3);
	num4 = num1 * ((num2 % 100) / 10);
	printf("%d\n", num4);
	num5 = num1 * (num2 / 100);
	printf("%d\n", num5);
	
	printf("%d", num3 + (num4 * 10) + (num5 * 100));

	return 0;
}