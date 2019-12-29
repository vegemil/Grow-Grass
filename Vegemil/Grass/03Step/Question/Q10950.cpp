#include "Q10950.h"
#include <iostream>
#include <vector>

void Q10950::start()
{
	int input = 0;
	std::cin >> input;
	
	int a = 0, b = 0;

	std::vector<int> result;

	for (int i = 0; i < input; ++i)
	{
		std::cin >> a >> b;

		result.push_back(a + b);
	}

	for (auto i : result)
	{
		std::cout << i << std::endl;
	}
}
