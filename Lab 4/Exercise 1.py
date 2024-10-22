def count_vowels(input_string):
    vowels = "aeiouAEIOUаеєиіїоуюяАЕЄИІЇОУЮЯ"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

assert count_vowels("hello") == 2
assert count_vowels("Привіт") == 2
assert count_vowels("universe") == 4
assert count_vowels("Львів") == 1

print("Усі тести пройдено успішно!")

