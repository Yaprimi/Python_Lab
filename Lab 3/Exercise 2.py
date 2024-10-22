while True:
    list1 = [int(n) for n in input('Введіть перший список цілих чисел через пробіл: ').split()]
    list2 = [int(m) for m in input('Введіть другий список цілих чисел через пробіл: ').split()]

    combined_list = sorted(list1 + list2, reverse=True)

    print('Об\'єднаний відсортований список у порядку спадання:', combined_list)
