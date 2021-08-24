#!/usr/bin/python3

"""Module brain-gcd."""

from brain_games.scripts.cli import welcom_user
from brain_games.scripts.general_functions import game_conditions, \
        receiving_response, checking_response
from brain_games.scripts.functions_for_brain_progression import creating_random_progression, \
        selecting_list_item



NAME_GAMES = 'progression'


def main():
    """Run brain-calc."""
    name = welcom_user()
    print(name)
    game_conditions(NAME_GAMES)
    number_of_correct_answers = 0
    flag = True
    NUMBER_OF_ANSWERS_TO_WIN = 3
    while flag is True:
        progression = creating_random_progression()
        hidden_item = selecting_list_item(progression)
        response = int(receiving_response())
        number_of_correct_answers = \
        checking_response(hidden_item, response,
                          number_of_correct_answers,
                          name)
        if number_of_correct_answers == NUMBER_OF_ANSWERS_TO_WIN:
            print('Congratulations, {}!'.format(name))
            flag = False
        elif number_of_correct_answers == 0:
            flag = False


if __name__ == '__main__':
    main()

