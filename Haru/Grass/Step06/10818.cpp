#include <cstdio>

int main()
{
	int caseNum;

	int min = 1000001;
	int max = -1000001;

	int num;
	int tmp = 0;

	scanf_s("%d\n", &caseNum);

	for (int i = 0; i < caseNum; i++)
	{
		scanf_s("%d", &num);

		if (num < min)
			min = num;

		if (num > max)
			max = num;
	}

	printf("%d %d", min, max);
}