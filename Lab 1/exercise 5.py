while True:
        a = float(input("Введіть довжину сторони a (або '0' для виходу): "))
        if a == 0:
            break
        b = float(input("Введіть довжину сторони b: "))
        c = float(input("Введіть довжину сторони c: "))
        
        if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
            print("Невірні сторони трикутника. Переконайтесь, що сторони задовольняють умову трикутника.")
            continue
        
        s = (a + b + c) / 2
        
        area_squared = s * (s - a) * (s - b) * (s - c)
        
        x = area_squared
        y = (x + 1) / 2
        while y < x:
            x = y
            y = (x + area_squared / x) / 2
        
        area1 = area_squared**0.5
        area = x
        
        print(f"Площа трикутника: {area:.5f} квадратних одиниць")
        print(f"Площа трикутника: {area1:.5f} квадратних одиниць")
    

print("Програма завершена.")
