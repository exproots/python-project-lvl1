#!/usr/bin/env python3
from random import randint


TASK_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_round():
    for i in range(0, 3):
        number = randint(1, 20)
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
    question = number
    return str(question), str(correct_answer)
