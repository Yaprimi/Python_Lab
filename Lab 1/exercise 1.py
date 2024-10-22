while True:
    number = int(input("Введіть чотиризначне число (або'0' для виходу): "))

    if number == 0:
            break
    
    if 1000 <= number <= 9999:
        total_sum = 0 
        while number > 0:
            total_sum += number % 10 
            number //= 10
            
        print("Сума цифр числа:", total_sum)

    else:
        print("Введіть коректне чотиризначне число.")

print("Програма завершена.")