#include <cstdio>

int main()
{
	int caseNum;
	int numOfStudent = 0;

	scanf_s("%d", &caseNum);

	for (int i = 0; i < caseNum; i++)
	{
		int arr[1000];
		int sum = 0;
		double average = 0.0;
		scanf_s("%d", &numOfStudent);

		for (int j = 0; j < numOfStudent; j++)
		{
			scanf_s("%d", &arr[j]);
			sum += arr[j];
		}
		average = (double)sum / numOfStudent;
		int cnt = 0;
		for (int t = 0; t < numOfStudent; t++)
		{
			if (average < arr[t]) {
				cnt++;
			}
		}		
		printf("%.3f%%\n", (double)cnt*100/numOfStudent);
	}
	return 0;
}