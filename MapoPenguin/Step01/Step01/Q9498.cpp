//���� ������ �Է¹޾� 90 ~100���� A, 80 ~89���� B, 70 ~79���� C, 60 ~69���� D, ������ ������ F�� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include "Q9498.h"

void Q9498()
{
	int score;

	scanf("%d", &score);

	if (score >= 90 && score <= 100)
		printf("A");
	else if (score >= 80 && score <= 89)
		printf("B");
	else if (score >= 70 && score <= 79)
		printf("C");
	else if (score >= 60 && score <= 69)
		printf("D");
	else
		printf("F");
}