#!/usr/bin/env python3
from random import randint


TASK_DESCRIPTION = 'Find the greatest common divisor of given numbers.'

first_number = 10
second_number = 20


def get_game_round():
    """Функция для определения целочистленного деления рандомных чисел!"""
    number1 = randint(first_number, second_number)
    number2 = randint(first_number, second_number)
    if number1 < number2:
        correct_answer = number1
    else:
        correct_answer = number2
    while correct_answer > 0:
        if number2 % correct_answer == 0 and number1 % correct_answer == 0:
            break
        correct_answer -= 1
    question = str(number1) + ' ' + str(number2)
    return str(question), str(correct_answer)
