#include <cstdio>

int main()
{
	int num1 = 0;
	int num2 = 0;
	int num3 = 0;

	scanf_s("%d %d %d", &num1, &num2, &num3);
	printf("%d\n", (num1+num2)%num3);
	printf("%d\n", (num1%num3 + num2%num3)%num3);
	printf("%d\n", (num1*num2)%num3);
	printf("%d", (num1%num3*num2%num3)%num3);

	return 0;
}