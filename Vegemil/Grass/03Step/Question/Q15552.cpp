#include "Q15552.h"
#include <vector>

void Q15552::start()
{
	std::cin.tie(NULL);
	std::cout.tie(NULL);
	std::ios_base::sync_with_stdio(false);

	int input = 0;
	int a = 0, b = 0;
	std::cin >> input;

	std::vector<int> result;

	for (int i = 0; i < input; ++i)
	{
		std::cin >> a >> b;

		result.push_back(a + b);
	}

	for (auto i : result)
	{
		std::cout << i << "\n";
	}
}
