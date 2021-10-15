from random import randint
from brain_games.logic_functions import welcome, get_name, answer_check
import prompt

TASK_DESCRIPTION = 'Find the greatest common divisor of given numbers.'

welcome()
name = get_name()
print(TASK_DESCRIPTION)
first_number = 1
second_number = 10


def find_gcd(number1, number2):
    """Функция для определения целочистленного деления рандомных чисел!"""
    if number1 < number2:
        true_answer = number1
    else:
        true_answer = number2

    while true_answer > 0:
        if number2 % true_answer == 0 and number1 % true_answer == 0:
            break
        true_answer -= 1
    return true_answer


def gcd():
    count_rounds = 3
    for i in range(count_rounds):
        number1 = randint(first_number, second_number)
        number2 = randint(first_number, second_number)
        print('Question: ' + str(number1) + ' ' + str(number2))
        true_answer = str(find_gcd(number1, number2))
        answer_correct = true_answer
        answer_user = prompt.string('You answer: ')
        answer_check(answer_user, answer_correct, name)
    print('Congratulations, ' + name + '!')
