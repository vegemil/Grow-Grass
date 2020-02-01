#include "Q2562.h"

void Q2562::start()
{
	int max = 0;
	int count = 0;
	int list[9];

	for (int i = 0; i < 9; ++i)
	{
		int num = 0;
		std::cin >> num;

		list[i] = num;

		if (max < list[i])
		{
			max = list[i];
			count = i;
		}
	}

	std::cout << max << std::endl;
	std::cout << count + 1;

}
