#include "Q10430.h"
#include <iostream>

void Q10430::start()
{
	int a, b, c;

	std::cin >> a >> b >> c;

	std::cout << (a + b) % c << std::endl;
	std::cout << ((a % c) + (b % c)) % c << std::endl;
	std::cout << (a * b) % c << std::endl;
	std::cout << (a % c * b % c) % c << std::endl;
}
