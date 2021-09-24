#!/usr/bin/env python3

# В этом файле объявим логические функции игр, которые будут постоянно использоваться
import prompt

rounds_count = 3


def welcome():
    print('Welcome to the Brain Games!')


def get_name():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def answer_check(answer_user, answer_correct, name):
    if answer_user == answer_correct:
        print('Correct!')
        return True
    else:
        print("'" + answer_user + "' is wrong answer ;(. Correct answer was '" + answer_correct + "'.")
        print("Let`s try again, " + name + "!")
        exit()
