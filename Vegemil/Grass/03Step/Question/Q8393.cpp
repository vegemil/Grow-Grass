#include "Q8393.h"
#include <iostream>

void Q8393::start()
{
	int input = 0;
	std::cin >> input;
	int result = 0;

	for (int i = 0; i < input; ++i)
	{
		result += i + 1;
	}

	std::cout << result;
}
