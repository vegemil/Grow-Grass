#include "Q10818.h"

#include <vector>
#include <algorithm>

void Q10818::start()
{
	int count = 0;
	std::cin >> count;

	std::vector<int> vec;
	for (int i = 0; i < count; ++i)
	{
		int num = 0;
		std::cin >> num;

		vec.push_back(num);
	}

	std::sort(vec.begin(), vec.end());

	std::cout << vec.at(0) << " " << vec.at(count - 1);
}
