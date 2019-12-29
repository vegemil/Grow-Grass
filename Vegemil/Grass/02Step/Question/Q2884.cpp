#include "Q2884.h"

void Q2884::start()
{
	int h, m;
	std::cin >> h >> m;

	m -= 45;

	if (m < 0)
	{
		h--;
		if (h < 0)
		{
			h = 23;
		}
		m = 60 + m;
	}

	std::cout << h << " " << m;
}
