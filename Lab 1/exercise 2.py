pi = 3.14159

while True:
        diameter = float(input("Введіть діаметр основи циліндра (в метрах): "))
        
        height = float(input("Введіть висоту циліндра (в метрах): "))

        paint_consumption = float(input("Введіть витрату фарби (літри на квадратний метр): "))
        
        if diameter <= 0 or height <= 0 or paint_consumption <= 0:
            print("Усі значення повинні бути позитивними числами.")
            continue
        
        radius = diameter / 2
        
        total_surface_area = 2 * pi * radius * (height + radius)
        
        total_paint_needed = total_surface_area * paint_consumption
        
        print(f"Площа поверхні циліндра: {total_surface_area:.2f} квадратних метрів")
        print(f"Загальна кількість фарби, необхідної для фарбування: {total_paint_needed:.2f} літрів")
    

print("Програма завершена.")
