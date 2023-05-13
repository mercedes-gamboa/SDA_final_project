"""1. Stwórz funkcję która przyjmuje jeden argument który ma być stringiem, funkcja powinna policzyć których znaków w stringu były najwięcej
i zwrócić znak oraz liczbę powtórzeń.
Np. dla stringa 'ala ma kota' wynikiem powinno być a, 4"""

duplicate_char = []
dup_counter = []
final_duplicates = {}

def find_duplicate(word):
    for char in word:
        if char not in duplicate_char and word.count(char) > 1:
            duplicate_char.append(char)
            dup_counter.append(word.count(char))

    for key in duplicate_char:
        for value in dup_counter:
            final_duplicates[key] = value
            dup_counter.remove(value)

    most_repeated = max(final_duplicates, key= lambda x: final_duplicates[x])
    highest_value = max(final_duplicates.values())

    print(f"The most repeated character is: {most_repeated} with a value of {highest_value}")


find_duplicate("ala ma kota")