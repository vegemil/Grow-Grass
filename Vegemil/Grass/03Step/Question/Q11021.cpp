#include "Q11021.h"

void Q11021::start()
{
	int input = 0;
	int a = 0, b = 0;

	std::cin >> input;

	for (int i = 0; i < input; ++i)
	{
		std::cin >> a >> b;
		std::cout << "Case #" << i + 1 << ": " << a + b << std::endl;
	}
}
