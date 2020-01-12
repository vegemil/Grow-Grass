#include <cstdio>

int main()
{
	int num = 0; //입력할 숫자
	int firstNum, secondNum; //첫번째 자리 숫자, 두 번째 자리 숫자
	int result = 0;
	int cycle = 0; //사이클 횟수

	scanf_s("%d", &num);

	result = num;

	while(1)
	{
		firstNum = result / 10;
		secondNum = result % 10;
		result = (secondNum * 10) + ((firstNum + secondNum) % 10);
		cycle++;

		if (num == result)
			break;
	}

	printf("%d\n", cycle);

	return 0;
}