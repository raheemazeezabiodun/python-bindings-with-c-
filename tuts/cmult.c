#include <stdio.h>
#include "cmult.h"


// a simple multiplication function that takes int and float parameters and return the float product
float cmult(int int_param, float float_param) {
    float return_value = int_param * float_param;
    printf("    In cmult : int: %d float %.1f returning  %.1f\n", int_param,
            float_param, return_value);
    return return_value;
}
