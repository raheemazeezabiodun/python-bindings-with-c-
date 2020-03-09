import invoke
from setuptools import setup, Extension
def print_banner(msg):
    print("==================================================")
    print("= {} ".format(msg))


@invoke.task
def generate_c_symbols(c):
    """ Build the shared library for the sample C++ code """
    print_banner("Building C Library Symbols for Python to use")
    invoke.run("gcc -c -Wall -Werror -fpic division.c -I /usr/include/python3.7")
    invoke.run("gcc -shared -o c_division.so division.o")
    print("* Complete")
