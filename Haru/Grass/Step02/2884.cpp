#include <cstdio>

int main()
{
	int h;
	int m;

	scanf_s("%d" "%d", &h, &m);

	if ((h < 0 || h > 23) || (m < 0 || m > 59))
		return 0;

	if (m > 45)
		printf("%d %d", h, m - 45);
	else if (m < 45)
	{
		if (h > 1)
			printf("%d %d", h - 1, m + 60 - 45);
		else
			printf("%d %d", 23, m + 60 - 45);
	}

	return 0;
}