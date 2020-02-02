#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int main()
{
    int caseNum, sum, count;
    char S[80];
    scanf_s("%d", &caseNum);

    for(int i = 0; i < caseNum; i++)
    {
        scanf_s("%s", S);
        sum = 0;
        count = 0;
        for (int j = 0; j < strlen(S); j++)
        {
            if (S[j] == 'O')
                count++;
            else
                count = 0;

            sum += count;
        }
        printf("%d\n", sum);
    }

    return 0;
}
