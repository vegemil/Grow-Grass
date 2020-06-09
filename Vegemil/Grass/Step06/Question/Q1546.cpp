#include "Q1546.h"

void Q1546::start()
{
	int temp = 0;
	std::cin >> temp;

	float* score = new float[temp];
	float* newScore = new float[temp];

	float max = 0;
	for (int i = 0; i < temp; ++i)
	{
		std::cin >> score[i];

		if (max < score[i])
		{
			max = score[i];
		}
	}

	float total = 0;

	for (int i = 0; i < temp; ++i)
	{
		newScore[i] = (score[i] / max) * 100;

		total += newScore[i];
	}


	std::cout << total / temp;
}

