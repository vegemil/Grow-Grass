#include "Q1110.h"

void Q1110::start()
{
	int firstNum, secondNum;
	int originalNum;

	std::cin >> originalNum;

	int cycle = 0;

	int newNumber = originalNum;

	while (true)
	{
		++cycle;
		firstNum = newNumber / 10;
		secondNum = newNumber % 10;

		newNumber = secondNum * 10 + ((firstNum + secondNum) % 10);
				
		if (newNumber == originalNum)
		{
			break;
		}		
	}

	std::cout << cycle;
}
