#!/usr/bin/env python3

# В этом файле объявим логические функции игр, которые будут постоянно использоваться
import prompt

rounds_count = 3


def get_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK_DESCRIPTION)
    count_rounds = 3
    step_round = 1

    while step_round <= count_rounds:
        question, correct_answer = game.get_game_round()
        print(f'Question: {question}')
        answer_user = prompt.string('You answer: ')
        if step_round == count_rounds and answer_user == correct_answer:
            print('Correct!')
            print('Congratulations, ' + name + '!')
        if answer_user == correct_answer and step_round != count_rounds:
            print('Correct!')
        else:
            if answer_user != correct_answer:
                print("'" + answer_user + "' is wrong answer ;(. Correct answer was '" + correct_answer + "'.")
                print("Let's try again, " + name + "!")
        step_round += 1
