//시험 점수를 입력받아 90 ~100점은 A, 80 ~89점은 B, 70 ~79점은 C, 60 ~69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
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