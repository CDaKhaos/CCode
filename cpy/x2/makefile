mcpp:
	g++ ctest.cpp -I /usr/include/python3.10 -L /usr/lib/python3.10/config-3.10-x86_64-linux-gnu -lpython3.10 -o main && ./main

mpyx:
	python setup.py build_ext --inplace

clear:
	rm -r build
	rm py.cpython-310-x86_64-linux-gnu.so main
