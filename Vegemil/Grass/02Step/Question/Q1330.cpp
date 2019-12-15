#include "Q1330.h"

void Q1330::start()
{
	int a, b;

	std::cin >> a >> b;

	if (a > b)
	{
		std::cout << ">" << std::endl;
	}
	else if (a < b)
	{
		std::cout << "<" << std::endl;
	}
	else if (a == b)
	{
		std::cout << "==" << std::endl;
	}
}
