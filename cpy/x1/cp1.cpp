#include <Python.h>
#include <iostream>
#include <ctime>
#include <cmath>
#include <vector>
#include <random>
using namespace std;

int python_sum(int i, int j);
int cpython_test(int i, int j);
int tset(int i,int j);
int tset1(int i,int j);

clock_t start_t, end_t;

int main()
{
	int c = tset(1, 2);

	int cpp = tset1(1, 2);

	Py_Initialize();
	if (!Py_IsInitialized())
	{
		cout << "Init faild/n" << endl;
	}
	int py = python_sum(1, 4);
	
	int cpy = cpython_test(1, 4);
	
	Py_Finalize();

	cout << "py-c:" << (double)py / (double)c*1.0  << endl;
	cout << "py-cpp:" << (double)py / (double)cpp*1.0  << endl;
	cout << "cpy-c:" << (double)cpy / (double)c*1.0  << endl;

	
	return 0;
}

int tset(int i,int j)
{
	start_t = clock();
	
	int LEN = 100*10000;
	double * pD = new double[LEN];
	srand(time(0));
	for(int i = 0; i < LEN; ++i)
	{
		double val = (double)(rand()) / RAND_MAX;
		pD[i] = sin(val);
	}
	delete[] pD;
	pD = nullptr;

	end_t = clock();
	clock_t aa = end_t - start_t;
	cout << "C rand:" << aa << "\n";
	return aa;
}

int tset1(int i,int j)
{
	start_t = clock();
	//生成[-1, 1]范围随机浮点数
	//模板参数只能是浮点类型（float，double， long double）
	int LEN = 100*10000;
	double * pD = new double[LEN];
	srand(time(0));
	uniform_real_distribution<double> u(-1, 1);
	default_random_engine e(time(NULL));
	for (size_t i = 0; i < LEN; ++i)
	{
		double val = u(e);
		pD[i] = sin(val);
	}
	delete[] pD;
	pD = nullptr;

	end_t = clock();
	clock_t aa = end_t - start_t;
	cout << "CPP random:" << aa << "\n";
	return aa;
}

int python_sum(int i, int j)
{
	start_t = clock();

	PyObject *pModule, *pFunc;
	PyObject *pArgs, *pValue;

	/* import */
	PyRun_SimpleString("import sys");
	PyRun_SimpleString("sys.path.append('./')");
	pModule = PyImport_ImportModule("py1");
	if (pModule == nullptr)
	{
		cout << "Module faild\n" << endl;
	}

	/* great_module.great_function */
	pFunc = PyObject_GetAttrString(pModule, "add");
	if (pFunc == nullptr)
	{
		cout << "Func faild\n" << endl;
	}

	/* build args */
	pArgs = PyTuple_New(2);
	PyTuple_SetItem(pArgs, 0, PyLong_FromLong(i));
	PyTuple_SetItem(pArgs, 1, PyLong_FromLong(j));

	/* call */
	pValue = PyObject_CallObject(pFunc, pArgs);
	
	//return PyLong_AsLong(pValue);
	int nListSize = PyList_Size(pValue);
	double* dArr = new double[nListSize];
	int a = 0;
	for (; a < nListSize; a++)
	{
		PyObject* pItem = PyList_GetItem(pValue, a);
		dArr[a] = PyFloat_AsDouble(pItem);
	}

	Py_DECREF(pArgs);
	Py_DECREF(pValue);
	delete[] dArr;
	dArr = nullptr;

	end_t = clock();
	clock_t aa = end_t - start_t;
	cout << "cpp-python:" << aa << "\n";

	return aa;
}

int cpython_test(int i, int j)
{
	start_t = clock();
	
	/* import */
	PyRun_SimpleString("import sys");
	PyRun_SimpleString("sys.path.append('./')");
	PyObject* pModule = PyImport_ImportModule("py");
	if (pModule == nullptr)
	{
		cout << "Module faild\n" << endl;
	}
	
	PyObject* pFunc = PyObject_GetAttrString(pModule, "add");
	if (pFunc == nullptr)
	{
		cout << "Func faild\n" << endl;
	}
	
	/* build args */
	PyObject* pArgs = PyTuple_New(2);
	PyTuple_SetItem(pArgs, 0, PyLong_FromLong(3));
	PyTuple_SetItem(pArgs, 1, PyLong_FromLong(4));

	/* call */
	PyObject* pValue = PyObject_CallObject(pFunc, pArgs);
	Py_DECREF(pArgs);
	
	int nListSize = PyList_Size(pValue);
	double* dArr = new double[nListSize];
	int a = 0;
	for (; a < nListSize; a++)
	{
		PyObject* pItem = PyList_GetItem(pValue, a);
		dArr[a] = PyFloat_AsDouble(pItem);
	}
	Py_DECREF(pArgs);
	Py_DECREF(pValue);
	delete[] dArr;
	dArr = nullptr;
	
	
	end_t = clock();
	clock_t aa = end_t - start_t;
	cout << "cpp-cpython:" << aa << "\n";

	return aa;
}
