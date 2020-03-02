#include "Q2577.h"

#include <string>

void Q2577::start()
{
	int num = 1;

    for(int i = 0; i < 3; ++i)
    {
        int temp = 0;
        std::cin >> temp;
        num *= temp;
    }

    int countList[10] = {0, };

    std::string resultNum = std::to_string(num);
    for (int i = 0; i < resultNum.size(); ++i)
    {
        auto n = resultNum.at(i) - '0';

        countList[n] += 1;
    }

    for (int i = 0; i < 10; ++i)
    {
        std::cout << countList[i] << std::endl;
    }
}
