"""A set of functions for brain-gcd."""

from random import randint


def creating_random_progression():
    """"Returns random progression"""
    length_pr = randint(8, 10)
    step_pr = randint(1, 10)
    first_pr = randint(0, 30)
    finish_pr = first_pr + length_pr * step_pr
    return [c for c in range(first_pr, finish_pr, step_pr)]


def selecting_list_item(progression):
    """Returns a hidden random element. \n
     Replacing it in the progression with '..'"""
    num_hidden_item = randint(1, (len(progression) - 1))
    hidden_item = progression[num_hidden_item]
    progression[num_hidden_item] = '..'
    print('Question: ', *progression)
    return hidden_item
