#!/usr/bin/env python3
from random import randint


TASK_DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

first_number = 1
second_number = 10


def check_prime(prime_number):
    """Функция для определения простого числа!"""
    k = 0
    for i in range(2, prime_number // 2 + 1):
        if (prime_number % i == 0):
            k += 1
    if (k <= 0):
        return True
    if prime_number < 2:
        return False
    else:
        return False


def get_game_round():
    prime_number = randint(first_number, second_number)
    correct_answer = 'yes' if check_prime(prime_number) else 'no'
    return str(prime_number), str(correct_answer)
