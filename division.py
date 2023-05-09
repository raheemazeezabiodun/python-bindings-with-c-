
from ctypes import *

def divide_numbers(a, b, library_path="libdivision.so"):
    libdivision = cdll.LoadLibrary(library_path)

    libdivision.divide_integers.argtypes = [c_int, c_int]
    libdivision.divide_integers.restype = c_float

    libdivision.divide_floats.argtypes = [c_float, c_float]
    libdivision.divide_floats.restype = c_float

    return {
        "integer_division": libdivision.divide_integers(a, b),
        "float_division": libdivision.divide_floats(c_float(a), c_float(b)),
    }