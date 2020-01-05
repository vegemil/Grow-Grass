#include <cstdio>

int main()
{
	int testcase;
	int num1, num2;

	scanf_s("%d", &testcase);

	for (int i = 1; i <= testcase; i++)
	{
		scanf_s("%d %d", &num1, &num2);
		printf("%s%d%s%d%s%d%s%d\n", "Case #", i, ": ", num1, " + ", num2, " = ", num1+num2);
	}
}