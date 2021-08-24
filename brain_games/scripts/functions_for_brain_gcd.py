"""A set of functions for brain-gcd."""

from random import randint


def output_random_number():
    """"Returns two random numbers"""
    num1 = randint(1, 20)
    num2 = randint(1, 20)
    print('Question: {} {}'.format(num1, num2))
    return [num1, num2]
