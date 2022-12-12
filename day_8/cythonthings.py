from setuptools import setup
from Cython.Build import cythonize


setup(
    name='day8AOC',
    ext_modules=cythonize("aocday8.pyx"),
    zip_safe=False,
)