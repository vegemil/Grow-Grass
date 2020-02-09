#include <cstdio>

int hansoo(int num)
{
	int arr[3];
	int result;

	if (num < 100)
		return num;

	result = 99;

	for (int i = 100; i <= num; i++)
	{
		if (i == 1000)
		{
			return result;
		}

		arr[0] = i / 100;
		arr[1] = (i / 10) - (arr[0] * 10);
		arr[2] = i % 10;

		if ((arr[0] - arr[1]) == (arr[1] - arr[2]))
		{
			result++;
		}
	}


	return result;
}

int main()
{
	int num;
	int result;

	scanf_s("%d", &num);

	if (num <= 0 || num > 1000)
		return -1;

	result = hansoo(num);
	printf("%d", result);

	return 0;
}