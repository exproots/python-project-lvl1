from random import randint, choice


TASK_DESCRIPTION = 'What number is missing in the progression?'

random_generate_number1 = 10
random_generate_number2 = 20


def get_game_round():
    random_number_progression = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    select_number = choice(random_number_progression)
    first_number = randint(random_generate_number1, random_generate_number2)
    progression = [x for x in range(first_number, first_number + select_number * 11, select_number)]
    number_prog2 = first_number + select_number
    number_prog3 = number_prog2 + select_number
    number_prog4 = number_prog3 + select_number
    number_prog5 = number_prog4 + select_number
    number_prog6 = number_prog5 + select_number
    number_prog7 = number_prog6 + select_number
    number_prog8 = number_prog7 + select_number
    number_prog9 = number_prog8 + select_number
    number_prog10 = number_prog9 + select_number
    numbers_progression = [first_number, number_prog2, number_prog3,
     number_prog4, number_prog5, number_prog6, number_prog7,
      number_prog8, number_prog9, number_prog10]
    hidden_number = choice(numbers_progression)
    question = ""
    for x in progression:
        if x == hidden_number:
            question += ".."
        else:
            question += str(x)
        if x != progression[-1]:
            question += " "
    correct_answer = str(hidden_number)
    return str(question), str(correct_answer)
