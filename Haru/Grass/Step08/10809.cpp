#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main()
{
	string s;
	cin >> s;

	int alphabet[26];

	memset(alphabet, -1, sizeof(alphabet));

	for (int i = 0; i < s.length(); i++)
	{
		if (alphabet[s[i] - 'a'] == -1)
		{
			alphabet[s[i] - 'a'] = i;
		}
	}

	for (int i = 0; i < 26; i++)
	{
		cout << alphabet[i] << " ";
	}
	cout << "\n";

	return 0;
}