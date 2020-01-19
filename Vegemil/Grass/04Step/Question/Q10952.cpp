#include "Q10952.h"

void Q10952::start()
{
	int a, b;

	while (true)
	{
		std::cin >> a >> b;

		if(a == 0 && b == 0) 
		{
			break;
		}

		std::cout << a + b << std::endl;
	}
}