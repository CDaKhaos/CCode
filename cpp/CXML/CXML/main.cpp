#include <stdio.h>
#include <vector>
#include <list>
#include <iostream>
#include <complex>

#include "XBMake.hpp"
using namespace SINUX;

#if _MSC_VER >=1600 //(1600 is VS2010)
#pragma execution_character_set("utf-8")
#endif

struct MyData
{
	int i;
    double d;
	char const * s;
	std::vector<int> vec;
	int iref;
    unsigned char uc;
    std::string ss;
    std::vector<float> vFloat;
    std::vector<std::string> vString;
    std::complex<float> comFloat;
	int flag;


    void setIntvalue(int in)
    {
		i = in;
	}
    int intvalue()
    {
		return i;
	}

    int & getIRef()
    {
		return iref;
	}

};

static XBind<MyData> const * GetXBind(MyData const &, Identity<MyData>)
{
	static XBindMember<MyData> binding;
	if (binding.empty())
	{
        binding.AddMember("COMPLEX", Member(&MyData::comFloat));
        binding.AddMember("VEC", Member(&MyData::vec));
        binding.AddMember("ITAG", Member(&MyData::i));
        binding.AddMember("ITAGGETSET", Member(&MyData::intvalue, &MyData::setIntvalue));
        binding.AddMember("DTAG", Member(&MyData::d));
        binding.AddMember("STAG", Member(&MyData::s));
        binding.AddMember("IREF", Member(&MyData::getIRef));
        binding.AddMember("uc", Member(&MyData::uc));
        binding.AddMember("ss", Member(&MyData::ss));
		binding.AddMember("Flag", Member(&MyData::flag));
        binding.AddMember("VEC_F", Member(&MyData::vFloat));
        binding.AddMember("VEC_S", Member(&MyData::vString));

	}
	return &binding;
}

class MyData2
{
public:
	MyData dataOne;
	MyData dataOne2;
	std::list<MyData> dataVec;
	int xyz;
};

static XBind<MyData2> const *
GetXBind(MyData2 const &, Identity<MyData2>)
{
	static XBindMember<MyData2> binding;
    if (binding.empty())
    {
		binding.AddMember("XYZ", MemberAttribute(&MyData2::xyz))->setFlags(MemberOptional);
		binding.AddMember("DATAONE", Member(&MyData2::dataOne));
		binding.AddMember("DATATWO", Member(&MyData2::dataOne2));
		binding.AddMember("DATAVEC", MemberPeer(&MyData2::dataVec));
	}
	return &binding;
}

int main(int argc, char *argv[])
{
	#ifdef QT
		QCoreApplication a(argc, argv);
	#endif // QT    

    MyData testData;
    testData.i = 100;
    testData.iref = 52;
    testData.d = 42.3;
    //testData.s = std::string("hello word中文测试").c_str();
	testData.s = "hello word";
    testData.uc = 255;
	testData.flag = 1;
    //testData.ss = std::string("mine is sljfdksj中文测试");
	testData.ss = std::string("mine is sljfdksj");
    testData.vec.push_back(05);
    testData.vec.push_back(1);
    testData.vec.push_back(2);
    testData.vec.push_back(3);
    testData.vec.push_back(5);


    testData.vFloat.push_back(10.1f);
    testData.vFloat.push_back(20.2f);

    testData.vString.push_back("30");
    testData.vString.push_back("40");

    testData.comFloat.real(1.0);
    testData.comFloat.imag(2.0);

    printf("\nTestData: %d %d %g %s %d\n", testData.i, testData.iref, testData.d, testData.s, testData.vec[0]);

	MakeXml("./1234.xml", testData);

    std::cout << "MakeXml" << "\n";

	MyData data2;
	ParseXml("./1234.xml", data2);
	printf("\ndata2: %d %d %g %s\n",
		data2.i, data2.iref, data2.d, data2.s);

    std::cout << "ParseXml" << "\n";

    int aaaa = 0;

	///////////////////////////////////////////////////////
	MyData2 testData3;
	testData3.xyz = 10342;
	testData3.dataOne = data2;
	testData3.dataOne2 = data2;
	testData3.dataVec.push_back(data2);
	testData3.dataVec.push_back(data2);
	MakeXml("./234.xml", testData3);

	MyData2 data21;
    ParseXml("./234.xml", data21);

	int b = 0;
#if 0


    MyData testData2;
	TiXmlElement pNewEle("NEW");
    BindFromXml(*pNewEle, &testData2);
    printf("\nTestData2: %d %d %g %s %d\n", testData2.i, testData2.iref, testData2.d, testData2.s, testData2.vec[0]);
    TiXmlElement testAgain("AGAIN");
    BindToXml(&testAgain, testData2);
    //testAgain.Print(stdout, 0);


    MyData2 testData3;
    testData3.xyz = 10342;
    testData3.dataOne = testData2;
    testData3.dataVec.push_back(testData2);
    testData3.dataVec.push_back(testData2);
    printf("\nTestData3: %i %i %g %s %s\n", testData3.xyz, testData3.dataOne.i,
        testData3.dataOne.d, testData3.dataOne.s, testData3.dataVec.front().s);

    TiXmlElement test2("TEST2");
    BindToXml(&test2, testData3);
    test2.Print(stdout, 0);
    MyData2 testData4;
    BindFromXml(test2, &testData4);
    printf("\nTestData4: %i %i %g %s %s\n", testData4.xyz, testData4.dataOne.i, testData4.dataOne.d,
        testData4.dataOne.s, testData4.dataVec.front().s);
	FILE *fp1 = NULL;
	fopen(&fp1, "D:\\234.xml", "w");
	test2.Print(fp1, 0);
	fclose(fp1);

    MyData2 testData5;
    test2.SetAttribute("XYZ", "");
    testData5.xyz = 0;
    BindFromXml(test2, &testData5);
    printf("\nTestData5: %i %i %g %s %s\n", testData5.xyz, testData5.dataOne.i, testData5.dataOne.d,
        testData5.dataOne.s, testData5.dataVec.front().s);
#endif

	#ifdef QT
		return a.exec();
	#else
		return 0;
	#endif // QT   
    
}
