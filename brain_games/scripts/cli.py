"""An example script."""

import prompt


def welcom_user():
    """Welcome user. Returns name user"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))  # noqa:P101
    return name
