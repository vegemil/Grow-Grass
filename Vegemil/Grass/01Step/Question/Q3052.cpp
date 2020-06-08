#include "Q3052.h"

void Q3052::start()
{
	bool remainder[42] = { false, };

	for (int i = 0; i < 10; ++i)
	{
		int temp = 0;
		std::cin >> temp;

		remainder[temp % 42] = true;
	}

	int count = 0;
	for (int i = 0 ; i < 42; ++i)
	{
		if (remainder[i])
		{
			++count;
		}
	}

	std::cout << count;
}

