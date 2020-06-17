#include "Q4673.h"
#include <string>


int Q4673::calNum(int num)
{
	auto strNum = std::to_string(num);

	int returnNum = num;
	for (auto str : strNum)
	{
		returnNum += str - '0';
	}

	return returnNum;
}

void Q4673::start()
{
	bool selfNumList[10000] = { false, };

	for (int i = 0; i < 10000; ++i)
	{
		int index = calNum(i);
		if (index >= 10000)
		{
			continue;
		}

		selfNumList[index] = true;
	}

	for (int i = 0; i < 10000; ++i)
	{
		if (false == selfNumList[i])
		{
			std::cout << i << std::endl;
		}
	}
}

