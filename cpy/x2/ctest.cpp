#include <dlfcn.h>
#include <iostream>
#include "Python.h"
using namespace std;

int main()
{
	setenv("PYTHONPATH", ".", 1);
	Py_Initialize();

	/* import */
	//PyRun_SimpleString("import sys");
	//PyRun_SimpleString("sys.path.append('./')");
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

	cout << "start-----------\n";
	clock_t start_t, end_t;
	start_t = clock();

	/* build args */
	PyObject* pArgs = PyTuple_New(2);
	PyTuple_SetItem(pArgs, 0, PyLong_FromLong(3));
	PyTuple_SetItem(pArgs, 1, PyLong_FromLong(4));

	/* call */
	PyObject* pValue = PyObject_CallObject(pFunc, pArgs);
	Py_DECREF(pArgs);
	
	int nListSize = PyList_Size(pValue);
	cout << "len:" << nListSize << endl;
	double* dArr = new double[nListSize];
	int a = 0;
	for (; a < nListSize; a++)
	{
		PyObject* pItem = PyList_GetItem(pValue, a);
		dArr[a] = PyFloat_AsDouble(pItem);
	}

	delete[] dArr;
	dArr = nullptr;


	//f_add(1, 2);
	
	

	end_t = clock();
	clock_t cc = end_t - start_t;
	cout << "AAAAAAAA:" << cc << "\n";

	Py_Finalize();
	return 1;
}
