#include <cstdio>

int main()
{
	int num = 0; //�Է��� ����
	int firstNum, secondNum; //ù��° �ڸ� ����, �� ��° �ڸ� ����
	int result = 0;
	int cycle = 0; //����Ŭ Ƚ��

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