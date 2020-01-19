#include "Q10871.h"
#include <vector>

void Q10871::start()
{
	int count = 0;
	int input = 0;

	std::cin >> count;
	std::cin >> input;

	std::vector<int> vec;

	for (int i = 0; i < count; ++i)
	{
		int temp = 0;
		std::cin >> temp;

		vec.push_back(temp);
	}

	for (auto num : vec)
	{
		if (num < input)
		{
			std::cout << num << " ";
		}
	}
}
