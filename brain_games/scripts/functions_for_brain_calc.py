"""A set of functions for brain-even."""

from random import randint


def generating_an_example():
    """"Returns two random numbers and a random operation"""
    POSSIBLE_OPERATIONS = ["+", "-", "*"]
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    operation = POSSIBLE_OPERATIONS[randint(0, 2)]
    print('Question: {} {} {}'.format(num1, operation, num2))
    return [num1, num2, operation]


def consider_correct_answer(num1, num2, operation):
    """Returns the result of evaluating the expression."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    return num1 * num2


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
