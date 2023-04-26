from setuptools import setup
from Cython.Build import cythonize

setup(
    name='exp',
    ext_modules=cythonize("py.pyx")
)
