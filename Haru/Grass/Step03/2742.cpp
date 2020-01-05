#include <cstdio>

int main() 
{
	int num;

	scanf_s("%d", &num);

	for (int i = num; i > 0; i--)
	{
		printf("%d\n", i);
	}
}