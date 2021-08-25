#!/usr/bin/python3

"""Module brain-calc."""

from brain_games.scripts.cli import welcom_user
from brain_games.scripts.general_functions import game_conditions,\
    receiving_response, checking_response
from brain_games.scripts.functions_for_brain_calc import\
    generating_an_example, consider_correct_answer

NAME_GAMES = 'calc'


def main():
    """Run brain-calc."""
    name = welcom_user()
    game_conditions(NAME_GAMES)
    number_of_correct_answers = 0
    flag = True
    NUMBER_OF_ANSWERS_TO_WIN = 3
    while flag is True:
        num1, num2, operation = generating_an_example()
        response = int(receiving_response())
        result = consider_correct_answer(num1, num2, operation)
        number_of_correct_answers = \
            checking_response(result, response,
                              number_of_correct_answers,
                              name)
        if number_of_correct_answers == NUMBER_OF_ANSWERS_TO_WIN:
            print('Congratulations, {}!'.format(name))
            flag = False
        elif number_of_correct_answers == 0:
            flag = False


if __name__ == '__main__':
    main()
