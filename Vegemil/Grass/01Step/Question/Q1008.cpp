#include "Q1008.h"

void Q1008::start()
{
	double a, b;
	std::cin >> a >> b;

	double result = a / b;

	std::cout << std::fixed;
	std::cout.precision(9);
	std::cout << result;
}
