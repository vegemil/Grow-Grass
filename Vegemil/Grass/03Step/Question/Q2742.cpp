#include "Q2742.h"

void Q2742::start()
{
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    std::ios_base::sync_with_stdio(false);

    int input = 0;
    std::cin >> input;

    for (int i = input; i > 0; --i)
    {
        std::cout << i << "\n";
    }

}
