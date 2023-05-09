

import ctypes

def float_division(dividend, divisor):
    libc = ctypes.CDLL("libc.so.6")
    libc.divf.argtypes = (ctypes.c_float, ctypes.c_float)
    libc.divf.restype = ctypes.c_float

    if divisor == 0:
        raise ZeroDivisionError("division by zero")

    result = libc.divf(ctypes.c_float(dividend), ctypes.c_float(divisor))
    return result

