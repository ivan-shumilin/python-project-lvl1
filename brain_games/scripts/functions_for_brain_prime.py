"""A set of functions for brain-even."""

from random import randint


def output_random_number():
    """Return rundom number from 1 to 100"""
    random_number = randint(1, 100)
    print('Question: {}'.format(random_number))
    return random_number


def is_number_prime(random_number):
    """"returns 'yes' if the number is prime otherwise 'no'"""
    if random_number == 1:
        return 'no'
    for i in range(2, random_number // 2 + 1):
        if random_number % i == 0:
            return 'no'
    return 'yes'
