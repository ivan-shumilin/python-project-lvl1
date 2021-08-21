#!/usr/bin/python3

"""Module brain-even."""

from brain_games.scripts.cli import welcom_user
from brain_games.scripts.general_functions import game_conditions,\
     receiving_response
from brain_games.scripts.functions_for_brain_even import\
     output_random_number, checking_response
from brain_games.scripts.functions_for_brain_even import is_number_even

NAME_GAMES = 'enev'


def main():
    """Run brain-even."""
    name = welcom_user()
    game_conditions(NAME_GAMES)
    number_of_correct_answers = 0
    flag = True
    NUMBER_OF_ANSWERS_TO_WIN = 3
    while flag is True:
        random_number = output_random_number()
        even_number = is_number_even(random_number)
        response = receiving_response()
        number_of_correct_answers = checking_response(even_number, name, number_of_correct_answers, response)  # noqa: E501
        if number_of_correct_answers == NUMBER_OF_ANSWERS_TO_WIN:
            print('Congratulations, {}!'.format(name))
            flag = False
        elif number_of_correct_answers == 0:
            flag = False


if __name__ == '__main__':
    main()
