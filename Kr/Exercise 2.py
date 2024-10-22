N = ord('Я') % 5 + 1
print(f"Варіант {N}")

def replace_with_zeros(list1, list2):
    list1[:] = [0 if elem in list2 else elem for elem in list1]
    return list1

list1 = [1.5, 2.3, 3.1, 4.7, 5.6]
list2 = [2.3, 4.7]

assert replace_with_zeros(list1, list2) == [1.5, 0, 3.1, 0, 5.6]

list3 = [2.7, 1.4, 6.9, 2.3, 9.1]
list4 = [1.4, 6.9, 2.7]

assert replace_with_zeros(list3, list4) == [0, 0, 0, 2.3, 9.1]

print("Усі тести пройдено успішно!")