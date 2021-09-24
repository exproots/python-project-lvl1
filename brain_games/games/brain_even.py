#!/usr/bin/env python3
import prompt
from random import randint


def even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(0, 3):
        number = randint(1, 20)
        print('Question: ' + str(number))
        answer_user = prompt.string('Your answer: ')
        if number % 2 == 0:
            answer_correct = 'yes'
        else:
            answer_correct = 'no'
        if answer_user == answer_correct:
            print('Correct!')
        else:
            print("'" + answer_user + "' is wrong answer ;(. Correct answer was '" + answer_correct + "'.")
            print("Let`s try again, " + name + "!")
            break
        if i == 2:
            print('Congratulations, ' + name + '!')
