#include "Q8958.h"

void Q8958::start()
{
	int count = 0;
	std::cin >> count;

	int* newScore = new int[count];

	for (int i = 0; i < count; ++i)
	{
		std::string text;
		std::cin >> text;

		int totalScore = 0;
		int score = 0;

		for(char var : text)
		{
			if (var == 'O')
			{
				totalScore += ++score;
			}
			else if (var == 'X')
			{
				score = 0;
			}
		}

		newScore[i] = totalScore;
	}

	for (int i = 0; i < count; ++i)
	{
		std::cout << newScore[i] << std::endl;
	}
}

