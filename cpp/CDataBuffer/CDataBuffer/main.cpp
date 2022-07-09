#include"CDataBuffer.h"
#include<iostream>
#include<string>
using namespace std;

struct test
{
	test()
	{
		a = 1;
		b = 2.1;
		c = 3.3;
		d = "4";
	}
	int a;
	float b;
	double c;
	string d;

	void Serial(CSunShine::CDataBuffer& dBuf)
	{
		dBuf << a;
		dBuf << b;
		dBuf << c;
		dBuf << d;
	}

	void DSerial(CSunShine::CDataBuffer& dBuf)
	{
		dBuf >> a;
		dBuf >> b;
		dBuf >> c;
		dBuf >> d;
	}
};

int main()
{
	test t;
	CSunShine::CDataBuffer dBuf;
	t.Serial(dBuf);
	size_t iLen = 0;
	char* pSend = dBuf.GetCharBuf(iLen);
	// --
	CSunShine::CDataBuffer dBuf1(pSend, iLen);
	test t1;
	t1.DSerial(dBuf1);

	getchar();
	return 0;
}
