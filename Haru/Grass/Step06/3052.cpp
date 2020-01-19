#include <cstdio>

int main()
{
	int check[42] = { 0, };

	int input;
	int result = 0;

	for(int i = 0; i < 10; i++)
	{
		scanf_s("%d", &input);
		check[input % 42] = 1;
	}

	for (int i = 0; i < 42; i++)
	{
		result += check[i];
	}

	printf("%d\n", result);
}