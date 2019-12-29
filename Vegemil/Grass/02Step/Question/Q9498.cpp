#include "Q9498.h"

void Q9498::start()
{
	int result;
	std::cin >> result;


	if (result >= 90)
	{
		std::cout << "A";
	}
	else if(result >= 80)
	{
		std::cout << "B";
	}
	else if (result >= 70)
	{
		std::cout << "C";
	}
	else if (result >= 60)
	{
		std::cout << "D";
	}
	else
	{
		std::cout << "F";
	}
}
