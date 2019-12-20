#include <cstdio>

int main()
{
	int score = 0;

	scanf_s("%d", &score);

	if (score < 0 || score > 100)
		return 0;

	if (score >= 90 && score <= 100)
		printf("%s\n", "A");
	else if (score >= 80 && score <= 89)
		printf("%s\n", "B");
	else if (score >= 70 && score <= 79)
		printf("%s\n", "C");
	else if (score >= 60 && score <= 69)
		printf("%s\n", "D");
	else
		printf("%s\n", "F");

	return 0;
}