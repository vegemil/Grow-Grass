#include "Q10951.h"

void Q10951::start()
{
	int a, b;

	while (true)
	{
		std::cin >> a >> b;

		if (std::cin.eof() == true) 
		{
			break;
		}

		std::cout << a + b << std::endl;

	}
}