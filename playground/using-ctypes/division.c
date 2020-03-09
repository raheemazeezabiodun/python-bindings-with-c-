#include <stdio.h>


float divide_numbers(int int_param, float float_param) {
    float return_value = int_param / float_param;
    printf("In C : int: %d divided by float %.1f =  %.1f\n", int_param,
            float_param, return_value);
    return return_value;
}
