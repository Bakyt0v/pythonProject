# Домашнее задание № 3
# Дан кортеж состоящий из разных типов данных:
# data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
# Создать два пустых списка letters и numbers
# Пройтись циклом for по кортежу data_tuple, добавить все строки в список letters, а всё остальное в numbers.
# Из списка numbers удалить число 6.13 и переместить True в конец списка letters, затем вставить число 2 между 3 и 1
# Отсортировать numbers, реверсировать letters и изменить пару букв в letters.
# Преобразовать списки numbers и letters в кортежи
# В итоге:
# кортеж letters должен выглядеть так:   (True, 'G', 'e', 'e', 'k', 'T', 'e', 'c', 'h')
# кортеж numbers должен выглядеть так:   (1, 2, 3)
# ДЗ 3 сохранить в .py файле под названием имя_homework_3

data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for i in data_tuple:
    if isinstance(i, bool):
        letters.append(i)
    elif isinstance(i, str):
        letters.append(i)
    else:
        numbers.append(i)
numbers.remove(6.13)
delete = letters.pop(4)
letters.append(delete)
numbers.insert(1, 2)
numbers.sort()
letters.reverse()
letters[1] = letters[1].title()
letters[7] = letters[7].lower()
data_letters = tuple(letters)
data_numbers = tuple(numbers)
print(data_letters)
print(data_numbers)
