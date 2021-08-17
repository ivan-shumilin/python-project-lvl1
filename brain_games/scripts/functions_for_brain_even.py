"""An example script."""

from random import randint
import prompt


def game_conditions():
    """Game conditions."""
    print('Answer "yes" if the number is even, otherwise answer "no".')


def output_random_number():
    random_number = randint(1, 100)
    print('Question: {}'.format(random_number))
    return random_number


def is_number_even(random_number):
    return 0 == random_number % 2


def checking_response(even_number, name, number_of_correct_answers):
    response = prompt.string('Your answer: ')
    if even_number is True:
        if response == "yes":
            print("Correct!")
            number_of_correct_answers = number_of_correct_answers + 1
            return number_of_correct_answers
        else:
            print("'{}' is wrong answer ;(. Correct answer was 'yes'.\
                \n Let's try again, {}!".format(response, name))
            number_of_correct_answers = 0
            return number_of_correct_answers
    if even_number is False:
        if response == "no":
            print("Correct!")
            number_of_correct_answers = number_of_correct_answers + 1
            return number_of_correct_answers
        else:
            print("'{}' is wrong answer ;(. Correct answer was 'no'.\
                \n Let's try again, {}!".format(response, name))
            number_of_correct_answers = 0
            return number_of_correct_answers
