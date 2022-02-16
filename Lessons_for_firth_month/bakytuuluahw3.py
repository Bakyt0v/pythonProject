data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
data_list = list(data_tuple)
del data_list[1:2]
deleted = data_list.pop(4)
data_list.append(deleted)
data_tuple = tuple(data_list)
for i in data_tuple:
    if isinstance(i, str):
        letters.append(i)
    else:
        numbers.append(i)
print(data_tuple)

