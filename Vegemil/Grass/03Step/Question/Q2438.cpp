#include "Q2438.h"

void Q2438::start()
{
	int input = 0;
	std::cin >> input;

	for (int i = 1; i <= input; ++i)
	{
		for (int j = 1; j <= i; ++j)
		{
			std::cout << "*";
		}

		std::cout << "\n";
	}
}
