"""A set of general functions."""

import prompt


def game_conditions(NAME_GAMES):
    """Accepts the name of the game. Returns the game condition."""
    if NAME_GAMES == 'enev':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif NAME_GAMES == 'calc':
        print('What is the result of the expression?')
    elif NAME_GAMES == 'gcd':
        print('Find the greatest common divisor of given numbers.')
    elif NAME_GAMES == 'progression':
        print('What number is missing in the progression?')


def receiving_response():
    """Returns the response entered by the user."""
    response = prompt.string('Your answer: ')
    return response


def checking_response(result, response, number_of_correct_answers, name):
    """"Return the result of checking the response"""
    if result == response:
        print("Correct!")
        number_of_correct_answers = number_of_correct_answers + 1
        return number_of_correct_answers
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.\
            \n Let's try again, {}!".format(response, result, name))
        number_of_correct_answers = 0
        return number_of_correct_answers
