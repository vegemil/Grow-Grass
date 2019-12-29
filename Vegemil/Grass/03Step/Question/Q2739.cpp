#include "Q2739.h"
#include <iostream>

void Q2739::start()
{
	int input;

	std::cin >> input;

	for (int i = 0; i < 9; ++i)
	{
		std::cout << input << " * " << i + 1 << " = " << input * (i + 1) << std::endl;
	}
}
