"""An example script."""

import prompt


def welcom_user():
    """Welcome user."""
    name = prompt.string('May I have your name?')
    print('Hello, {}'.format(name))  # noqa:P101
