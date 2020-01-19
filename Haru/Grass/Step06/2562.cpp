#include <cstdio>

int main()
{
	int numArray[9];
	int index;
	int maxNum = 0;

	for (int i = 0; i < 9; i++)
	{
		scanf_s("%d", &numArray[i]);

		if (maxNum < numArray[i])
		{
			maxNum = numArray[i];
			index = i + 1;
		}

	}

	printf("%d\n%d", maxNum, index);
}