#include "Q4344.h"

void Q4344::start()
{
	int count = 0;
	std::cin >> count;

	float* output = new float[count];

	for (int i = 0; i < count; ++i)
	{
		int studentNum = 0;
		std::cin >> studentNum;

		int* score = new int[studentNum];
		int totalScore = 0;

		for (int j = 0; j < studentNum; ++j)
		{
			std::cin >> score[j];

			totalScore += score[j];
		}


		int avg = totalScore / studentNum;
		float temp = 0.f;
		for (int j = 0; j < studentNum; ++j)
		{
			if (avg < score[j])
			{
				temp++;
			}
		}
		  
		float totalAvg = temp / studentNum * 100.f;
		
		output[i] = totalAvg;

		delete[] score;
	}

	for (int i = 0; i < count; ++i)
	{
		printf("%.3f%%\n", output[i]);
	}

	delete[] output;
}

