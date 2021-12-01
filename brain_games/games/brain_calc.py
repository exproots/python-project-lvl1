#!/usr/bin/env python
from random import randint, choice

TASK_DESCRIPTION = 'What is the result of the expression?'


def get_game_round():
    count_rounds = 3
    operator_list = ['+', '-', '*']
    for i in range(count_rounds):
        question_number = randint(10, 30)
        question_number2 = randint(1, 10)
        question_operator = choice(operator_list)
        if question_operator == '+':
            correct_answer = str(question_number + question_number2)
        elif question_operator == '-':
            correct_answer = str(question_number - question_number2)
        else:
            correct_answer = str(question_number * question_number2)
        question = str(question_number) + ' ' \
            + question_operator + ' ' + str(question_number2)
        return str(question), str(correct_answer)
