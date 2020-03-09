import ctypes
import pathlib

if __name__ == "__main__":
    libname = pathlib.Path().absolute() / "c_division.so"
    c_lib = ctypes.CDLL(libname)

    x, y = 6, 2.3
    c_lib.divide_numbers.restype = ctypes.c_float
    answer = c_lib.divide_numbers(x, ctypes.c_float(y))
    print(f"In Python: int: {x} divided by float {y:.1f} = {answer:.1f}")
