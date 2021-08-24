"""A set of functions for brain-even."""

from random import randint

def output_random_number():
    """Return rundom number from 1 to 100"""
    random_number = randint(1, 100)
    print('Question: {}'.format(random_number))
    return random_number


def is_number_prime(random_number):
    """"Return check the number for the presence of parity """
    if random_number % 2 == 0:
        return 'yes'
    else:
        return 'no'