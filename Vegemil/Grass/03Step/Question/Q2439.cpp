#include "Q2439.h"

void Q2439::start()
{
	int input = 0;
	std::cin >> input;

	for (int i = 1; i <= input; ++i)
	{
		for (int j = 1; j <= input; ++j)
		{
			if (j > input - i)
			{
				std::cout << "*";
			}
			else
			{
				std::cout << " ";
			}
		}
				
		std::cout << "\n";
	}
}
