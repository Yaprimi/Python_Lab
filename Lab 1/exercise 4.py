while True:
        angle1 = float(input("Введіть перший кут трикутника (або '0' для виходу): "))
        if angle1 == 0:
            break
        
        angle2 = float(input("Введіть другий кут трикутника: "))
        
        if angle1 <= 0 or angle2 <= 0 or angle1 + angle2 >= 180:
            print("Кути повинні бути позитивними, а їх сума менше 180 градусів.")
            continue
        
        angle3 = 180 - (angle1 + angle2)

        print(f"Третій кут трикутника: {angle3:.0f} градусів")
    

print("Програма завершена.")
