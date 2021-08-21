"""A set of general functions."""

import prompt


def game_conditions(NAME_GAMES):
    """Accepts the name of the game. Returns the game condition."""
    if NAME_GAMES == 'enev':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif NAME_GAMES == 'calc':
        print('What is the result of the expression?')


def receiving_response():
    """Returns the response entered by the user."""
    response = prompt.string('Your answer: ')
    return response
