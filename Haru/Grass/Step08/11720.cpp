#include <cstdio>

int main()
{
	int digit;
	scanf_s("%d", &digit);

	int sum = 0;
	char num[100];
	scanf_s("%s", &num);

	for (int i = 0; i < digit; i++)
	{
		sum += (num[i] - '0'); //-48
	}
	printf("%d\n", sum);
	return 0;
}