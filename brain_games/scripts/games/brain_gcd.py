#!/usr/bin/python3

"""Module brain-gcd."""

from brain_games.scripts.cli import welcom_user
from brain_games.scripts.general_functions import game_conditions,\
      receiving_response, checking_response
from brain_games.scripts.functions_for_brain_gcd import \
    output_random_number, gcd_rem_division
# import fractions

NAME_GAMES = 'gcd'


def main():
    """Run brain-gcd."""
    name = welcom_user()
    print(name)
    game_conditions(NAME_GAMES)
    number_of_correct_answers = 0
    flag = True
    NUMBER_OF_ANSWERS_TO_WIN = 3
    while flag is True:
        num1, num2 = output_random_number()
        response = int(receiving_response())
        result = gcd_rem_division(num1, num2)
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
