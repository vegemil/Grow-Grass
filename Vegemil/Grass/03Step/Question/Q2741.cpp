#include "Q2741.h"

void Q2741::start()
{
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    std::ios_base::sync_with_stdio(false);

    int input = 0;
    std::cin >> input;

    for (int i = 0; i < input; ++i)
    {
        std::cout << i + 1 << "\n";
    }

}
