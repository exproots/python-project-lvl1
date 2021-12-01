#!/usr/bin/env python3
from random import randint


TASK_DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

first_number = 1
second_number = 10


def check_prime(prime_number):
    """Функция для определения простого числа!"""
    first_prime = 2
    if prime_number % 2 == 0:
        return False
    if prime_number < first_prime:
        return False
    d = 3
    if prime_number == 9:
        return False
    while d * d <= prime_number and prime_number % d != 0:
        d += 1
    return True


def get_game_round():
    prime_number = randint(first_number, second_number)
    correct_answer = 'yes' if check_prime(prime_number) else 'no'
    return str(prime_number), str(correct_answer)
