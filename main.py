import numpy as np


def game_core_v3(number):
    global count  # счётчик попыток виден глобально
    count = 0
    numb_list = [i for i in range(1, 101)]  # генерируем список 1-100
    search_alg(numb_list, number)  # вызов рекурсивной функции для поиска числа
    print(count)
    return count


def search_alg(list, n):  #
    left = 0
    right = len(list) - 1
    predict = (left + right) // 2  # предпологаемое число
    print(list[predict], "-")
    global count
    count += 1
    if (n == list[predict]):
        return count
    # Check right side of arr
    if (n > list[predict]):  # проверяем если искомое больше предполагаемого
        return search_alg(list[predict + 1:], n) + (predict + 1)

    else:  # искомое меньше предполагаемого
        return search_alg(list[:predict], n)


def score_game(game_core):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


score_game(game_core_v3)

