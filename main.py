import numpy as np


def game_core_v1(number):
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)
        if number == predict:
            return count


def score_game(game_core):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core_v1)

