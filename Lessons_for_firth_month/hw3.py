data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)
numbers.remove(numbers[0])
numbers.insert(2, 2)
deleted = numbers.pop(0)
letters.append(deleted)
numbers.sort()
letters.reverse()
letters[1] = 'G'
letters[7] = 'c'
letters = tuple(letters)
numbers = tuple(numbers)
print(letters)
print(numbers)
isinstance(i, str)