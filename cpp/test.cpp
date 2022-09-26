#include<iostream>
using namespace std;

int main()
{
#ifdef __linux__
	cout << "linux" << endl;
#elif _WIN32
	cout << "windows" << endl;
#endif
	return 0;
}
