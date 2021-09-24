#!/usr/bin/env python
from random import randint, choice
from brain_games.logic_functions import welcome, get_name, answer_check
import prompt

welcome()
name = get_name()
QUESTION_TASK = 'What is the result of the expression?'
print(QUESTION_TASK)


def calc():
    count_rounds = 3
    operator_list = ['+', '-', '*']
    for i in range(count_rounds):
        question_number = randint(10, 30)
        question_number2 = randint(1, 10)
        question_operator = choice(operator_list)
        print('Question: ' + str(question_number) + ' ' + question_operator + ' ' + str(question_number2))
        answer_user = prompt.string('Your answer: ')
        if question_operator == '+':
            answer_correct = str(question_number + question_number2)
        elif question_operator == '-':
            answer_correct = str(question_number - question_number2)
        else:
            answer_correct = str(question_number * question_number2)
        answer_check(answer_user, answer_correct, name)
    print('Congratulations, ' + name + '!')
