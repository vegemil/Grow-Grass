#include "Q10817.h"
#include <algorithm>
#include <vector>

void Q10817::start()
{
	std::vector<int> input;

	for (int a = 0; a < 3; ++a)
	{
		int put = 0;
		std::cin >> put;
		input.push_back(put);
	}

	std::sort(input.begin(), input.end());

	std::cout << input.at(1);
}
