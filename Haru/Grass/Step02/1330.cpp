#include <cstdio>

int main()
{
	int num1 = 0;
	int num2 = 0;

	scanf_s("%d %d", &num1, &num2);
	
	if (num1 > num2)
		printf("%s\n", ">");
	else if (num1 < num2)
		printf("%s\n", "<");
	else
		printf("%s\n", "==");

	return 0;
}