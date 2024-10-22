while True:
    numbers = [int(x) for x in input('Введіть список цілих чисел через пробіл: ').split()]

    for num in numbers[:]:
        if numbers.count(num) == 1:
            numbers.remove(num)

    print('Список без унікальних елементів:', numbers)
