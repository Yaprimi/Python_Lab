import math
N = ord('Я') % 5 + 1
print(f"Варіант {N}")
def compute_y_values(interval):
    step = 0.2
    x = interval[0]
    y_values = []
    
    while x <= interval[1]:
        if x > 1:
            y = math.sqrt(math.tan(x**2 - 1))
        elif 0 <= x <= 1:
            y = -2 * x
        elif x < 1:
            y = math.exp(math.cos(x))
        y_values.append(y)
        x += step
    
    return y_values

interval = [-1, 1.5]
result = compute_y_values(interval)
for y_val in result:
    print(f"y = {y_val}")
