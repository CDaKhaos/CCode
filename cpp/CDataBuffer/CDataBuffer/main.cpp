#include "CAllData.h"

#include<thread>
#include<windows.h>
#include<iostream>
using namespace std;

void f1(int n)
{
	for (int i = 0; i < 500; ++i) {
		std::cout << "Thread " << n << " executing\n";
		//std::this_thread::sleep_for(std::chrono::milliseconds(10));
	}
}

// 设置线程优先级
/*
#define THREAD_PRIORITY_LOWEST          THREAD_BASE_PRIORITY_MIN
#define THREAD_PRIORITY_BELOW_NORMAL    (THREAD_PRIORITY_LOWEST+1)
#define THREAD_PRIORITY_NORMAL          0
#define THREAD_PRIORITY_HIGHEST         THREAD_BASE_PRIORITY_MAX
#define THREAD_PRIORITY_ABOVE_NORMAL    (THREAD_PRIORITY_HIGHEST-1)
#define THREAD_PRIORITY_ERROR_RETURN    (MAXLONG)
*/
static bool setPriority(std::thread &th, int priority = THREAD_PRIORITY_HIGHEST)
{
	HANDLE hand = th.native_handle();
	SetThreadPriority(hand, priority);
	return priority == GetThreadPriority(hand);
}


int main()
{
	cout << "begin" << endl;
	thread a(f1, 2);
	thread b(f1, 1);
	bool bb = setPriority(b, THREAD_PRIORITY_HIGHEST);

	/*
	CAllData all;

	CSoldier s1;
	s1.m_nLive = 1;
	all.m_vSoldier.push_back(s1);
	s1.m_nLive = 2;
	all.m_vSoldier.push_back(s1);

	CUav u1;
	u1.A = "123";
	all.m_vUav.push_back(u1);
	u1.A = "234";
	all.m_vUav.push_back(u1);
	u1.A = "345";
	all.m_vUav.push_back(u1);

	size_t iLen = 0;;
	char* pBuf = all.GetSendBuf(iLen);

	CAllData all1(pBuf, iLen);*/

	getchar();
	return 0;
}
