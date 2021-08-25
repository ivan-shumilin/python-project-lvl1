#!/usr/bin/python3

"""Module brain-prime."""

from brain_games.scripts.cli import welcom_user
from brain_games.scripts.general_functions import game_conditions,\
    receiving_response, checking_response, output_random_number
from brain_games.scripts.functions_for_brain_prime import \
    is_number_prime

NAME_GAMES = 'prime'


def main():
    """Run brain-prime."""
    name = welcom_user()
    game_conditions(NAME_GAMES)
    number_of_correct_answers = 0
    flag = True
    NUMBER_OF_ANSWERS_TO_WIN = 3
    while flag is True:
        random_number = output_random_number()
        result = is_number_prime(random_number)
        response = receiving_response()
        number_of_correct_answers = checking_response(result, response, number_of_correct_answers, name)  # noqa: E501
        if number_of_correct_answers == NUMBER_OF_ANSWERS_TO_WIN:
            print('Congratulations, {}!'.format(name))
            flag = False
        elif number_of_correct_answers == 0:
            flag = False


if __name__ == '__main__':
    main()
