def clean_text(text):
    symbols_to_remove = [".", ",", "\n", "(", ")", "'", ":", ";", "!", "?", "-", "_", "\"","/","`"]
    for symbol in symbols_to_remove:
        text = text.replace(symbol, " ")
    for symbol in "’":
            text = text.replace(symbol, "")

    return text.lower()

def count_words_in_file(file_path):
    with open(file_path) as file:
        text = file.read()
        
    cleaned_text = clean_text(text)

    words = cleaned_text.split()

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

def find_most_frequent_word(word_count_dict):
    most_frequent_word = max(word_count_dict, key=word_count_dict.get)
    return most_frequent_word, word_count_dict[most_frequent_word]

def sort_dict_by_keys(word_count_dict):
    sorted_dict = dict(sorted(word_count_dict.items(), key=lambda item: item[0]))
    return sorted_dict

def sort_dict_by_values(word_count_dict):
    sorted_dict = dict(sorted(word_count_dict.items(), key=lambda item: item[1]))
    return sorted_dict

file_path = 'C:/text.txt'
word_count_dict = count_words_in_file(file_path)

most_frequent_word, frequency = find_most_frequent_word(word_count_dict)
print(f"Найуживаніше слово: '{most_frequent_word}' зустрічається {frequency} раз(ів).")

for word, count in word_count_dict.items():
    print(f"{word} : {count}")
print("\n")

sorted_word_count_dict = sort_dict_by_keys(word_count_dict)

print("Словник, відсортований за ключами:")
for word, count in sorted_word_count_dict.items():
    print(f"{word} : {count}")

print("\n")
sorted_word_count_dict = sort_dict_by_values(word_count_dict)

print("Словник, відсортований за значеннями:")
for word, count in sorted_word_count_dict.items():
    print(f"{word} : {count}")