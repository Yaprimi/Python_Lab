def create_dict(n):
    return {str(i): i for i in range(1, n+1)}

assert create_dict(5) == {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
assert create_dict(3) == {'1': 1, '2': 2, '3': 3}
assert create_dict(1) == {'1': 1}

print("Усі тести пройдено успішно!")
