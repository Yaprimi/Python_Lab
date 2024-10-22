while True:
        n = int(input("Введіть кількість учнів (або '0' для виходу): "))
        if n == 0:
            break

        k = int(input("Введіть кількість яблук: "))
        
        if n <= 0 or k < 0:
            print("Кількість учнів має бути більшою за нуль, а кількість яблук не може бути від'ємною.")
            continue

        apples_per_student = k // n
        apples_left = k % n


        print(f"Кожен учень отримає {apples_per_student} яблук.")
        print(f"В кошику залишилося {apples_left} яблук.")

print("Програма завершена.")
