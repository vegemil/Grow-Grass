#include <cstdio>
#define MAX 10001
bool arr[MAX];

int solution(int n)
{
	int result = n;

	while (true)
	{
		if (n == 0) break;
		result += n % 10;
		n = n / 10;
	}

	return result;
}

int main()
{
	for (int i = 0; i < MAX; i++)
	{
		int index = solution(i);

		if (index <= MAX)
		{
			arr[index] = true;
		}
	}

	for (int i = 0; i < MAX; i++)
	{
		if (!arr[i])
		{
			printf("%d\n", i);
		}
	}
	return 0;
}