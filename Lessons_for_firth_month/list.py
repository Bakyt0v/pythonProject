data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for i in data_tuple:
    if isinstance(i, str):
        letters.append(i)
    else:
        numbers.append(i)
deleted = numbers.pop(1)
letters.append(deleted)
del numbers[0:1]
numbers.insert(1, 2)
letters.reverse()
numbers.sort()
letters[1] = letters[1].title()
letters[7] = letters[7].lower()
letters_tuple = tuple(letters)
numbers_tuple = tuple(numbers)
print(letters_tuple)
print(numbers_tuple)

