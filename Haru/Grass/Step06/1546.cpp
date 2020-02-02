#include <cstdio>

int main()
{
	int caseNum;
	float sum = 0;
	float max = 0.0;

	scanf_s("%d", &caseNum);

	int *ary = new int[caseNum];

	for (int i = 0; i < caseNum; i++)
	{
		scanf_s("%d", &(ary[i]));

		if (max < ary[i])
			max = ary[i];
	}

	for (int i = 0; i < caseNum; i++)
	{
		sum += (ary[i]/max) * 100;
	}

	printf("%f.2", (float)(sum / caseNum));
}