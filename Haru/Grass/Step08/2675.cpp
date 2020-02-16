#include <iostream>
#include <string>

using namespace std;

int main()
{
	int caseNum;
	cin >> caseNum;

	for (int i = 0; i < caseNum; i++)
	{
		int R;
		cin >> R;
		string S;
		cin >> S;

		for(int j = 0; j < S.length(); j++)
		{
			for (int k = 0; k < R; k++)
			{
				cout << S[j];
			}
		}
		cout << "\n";
	}

	return 0;
}