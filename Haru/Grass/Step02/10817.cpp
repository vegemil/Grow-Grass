#include <cstdio>

int main()
{
	int num1;
	int num2;
	int num3;

	int answer;

	scanf_s("%d %d %d", &num1, &num2, &num3);

	if (num1 < num2)
		if (num1 > num3)
			answer = num1;
		else
			if (num2 > num3)
				answer = num3;
			else
				answer = num2;
	else
		if (num1 < num3)
			answer = num1;
		else
			if (num2 > num3)
				answer = num2;
			else
				answer = num3;

	printf("%d", answer);

	return 0;
}