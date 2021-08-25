"""A set of functions for brain-gcd."""

from random import randint


def output_random_number():
    """"Returns two random numbers"""
    num1 = randint(1, 20)
    num2 = randint(1, 20)
    print('Question: {} {}'.format(num1, num2))
    return [num1, num2]
    

def gcd_rem_division(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2