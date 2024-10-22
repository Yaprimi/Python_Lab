
def calculate_total_price(price):
    discount = 0
    
    if price > 2000:
        discount = 0.20
    elif price > 1000:
        discount = 0.10
    
    
    final_price = price * (1 - discount)
    return final_price

while True:
    purchase_price = int(input("Введіть вартість покупки (грн)(або'0' для виходу): "))

    if purchase_price == 0:
                break

    total_price = calculate_total_price(purchase_price)

    print(f"Вартість покупки після знижки: {total_price:.2f} грн")

print("Програма завершена.")