"""A set of functions for brain-even."""

from random import randint


def output_random_number():
    """Return rundom number from 1 to 100"""
    random_number = randint(1, 100)
    print('Question: {}'.format(random_number))
    return random_number


def is_number_even(random_number):
    """"Return check the number for even """
    if random_number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def checking_response(even_number, name, number_of_correct_answers, response):
    """"Return the result of checking the response"""
    if even_number == 'yes':
        if response == 'yes':
            print("Correct!")
            number_of_correct_answers = number_of_correct_answers + 1
            return number_of_correct_answers
        else:
            print("'{}' is wrong answer ;(. Correct answer was 'yes'.\
                \n Let's try again, {}!".format(response, name))
            number_of_correct_answers = 0
            return number_of_correct_answers
    if even_number == 'no':
        if response == 'no':
            print("Correct!")
            number_of_correct_answers = number_of_correct_answers + 1
            return number_of_correct_answers
        else:
            print("'{}' is wrong answer ;(. Correct answer was 'no'.\
                \n Let's try again, {}!".format(response, name))
            number_of_correct_answers = 0
            return number_of_correct_answers
