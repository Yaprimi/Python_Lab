def analyze_number(num):
    a = num // 100
    b = (num // 10) % 10
    c = num % 10
    
    digit_sum = a + b + c
    digit_product = a * b * c
    
    is_double_digit_sum = 10 <= digit_sum <= 99
    is_triple_digit_product = 100 <= digit_product <= 999
    
    return is_double_digit_sum, is_triple_digit_product

while True:
    N = ord("Я") % 5 + 1
    print(f"Варіант: {N}")

    number = int(input("Введіть тризначне число (або '0' для виходу): "))
    
    if number == 0:
        break
    
    if 100 <= number <= 999:
        sum_is_double_digit, product_is_triple_digit = analyze_number(number)

        print(f"Сума цифр є двозначним числом: {sum_is_double_digit}")
        print(f"Добуток цифр є тризначним числом: {product_is_triple_digit}")
    else:
        print("Введіть коректне тризначне число.")

print("Програма завершена.")
