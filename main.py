import numpy as np


def game_core_v3(number):
    global count  # счётчик попыток виден глобально
    count = 0
    numb_list = [i for i in range(1, 101)]  # генерируем список 1-100
    search_alg(numb_list, number)  # вызов рекурсивной функции для поиска числа
    print(count) # вывод количества попыток для поиска каждого number
    return count


def search_alg(list, n):  # рекурсивная функция для бинарного поиска элемента в списке
    left = 0
    right = len(list) - 1
    predict = (left + right) // 2  # предпологаемое число
    print(list[predict], "-") # вывод предпологаемого числа
    global count
    count += 1
    if (n == list[predict]):
        return count
    # Check right side of arr
    if (n > list[predict]):  # проверяем если искомое больше предполагаемого
        return search_alg(list[predict + 1:], n) + (predict + 1)  # возвращаем вызов функции со списком и смещением индекса
    else:  # искомое меньше предполагаемого
        return search_alg(list[:predict], n)  # возвращаем вызов функции со списком от первого элемента до предпологаем


def score_game(game_core):
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(count_ls)  # вывод списка количества попыток необходимых алгоритму для угадывания
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


score_game(game_core_v3)

