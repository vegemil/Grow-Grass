#include <cstdio>

int main()
{
	int year = 0;

	scanf_s("%d", &year);

	if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
		printf("%d", 1);
	else
		printf("%d", 0);

	return 0;
}