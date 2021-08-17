#!/usr/bin/python3

"""An example script."""

from brain_games.scripts.cli import welcom_user
from brain_games.scripts.functions_for_brain_even import game_conditions
from brain_games.scripts.functions_for_brain_even import output_random_number
from brain_games.scripts.functions_for_brain_even import checking_response
from brain_games.scripts.functions_for_brain_even import is_number_even


def main():
    """Run an example code."""
    name = welcom_user()
    game_conditions()
    number_of_correct_answers = 0
    flag = True
    while flag is True:
        random_number = output_random_number()
        even_number = is_number_even(random_number)
        number_of_correct_answers = checking_response(even_number, name, number_of_correct_answers)  # noqa: E501
        if number_of_correct_answers == 3:
            print('Congratulations, {}!'.format(name))
            flag = False
        elif number_of_correct_answers == 0:
            flag = False


if __name__ == '__main__':
    main()
