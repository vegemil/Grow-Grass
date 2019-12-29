#include "Q2753.h"

void Q2753::start()
{
	int result;
	std::cin >> result;

	if (result % 4 == 0 && (result % 100 != 0 || result % 400 == 0))
	{
		std::cout << "1";
	}
	else
	{
		std::cout << "0";
	}
}
