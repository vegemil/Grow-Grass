#include "Q11022.h"

void Q11022::start()
{
	int input = 0;
	int a = 0, b = 0;

	std::cin >> input;

	for (int i = 0; i < input; ++i)
	{
		std::cin >> a >> b;
		std::cout << "Case #" << i + 1 << ": " << a << " + " << b << " = " << a + b << std::endl;
	}
}
