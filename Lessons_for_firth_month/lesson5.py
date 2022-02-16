# students = [
#     {'name': 'Aman', 'hw': 5, 'deadl': True, 'points': 39, 'last_rate': 10},
#     {'name': 'Dilyar', 'hw': 5, 'deadl': True, 'points': 39, 'last_rate': 10},
#     {'name': 'Amantur', 'hw': 5, 'deadl': True, 'points': 39, 'last_rate': 10},
#     {'name': 'Atabek', 'hw': 5, 'deadl': False, 'points': 39, 'last_rate': 10}
# ]
# students[0]['name' ='Amanbek'

#
# def fs(name = 'None'):
#     for i in students:
#         if name in i.values():
#             return i
#         else:
#             return False

# def edit(name, newname):
#     if fs(name):
#         students[students.index(fs(name))]['name'] = newname
#     else:
#         print('Ns')
# edit('Dilyar', 'Dil')
# Вызов функции внутри списка
# def delete(name):
#     if fs(name):
#         students.remove(fs(name))
#     else:
#         print('no student')
# delete('Aman')
#
#
#
#
# name = input('Введите name:')
# for i in students:
#     if name in i.values():
#         students.remove(i)
# del students[3]
# def cheker():
#     for i in students:
#         if i['deadl'] == True:
#             i['last_rate'] = 10
#             i['points'] += i['last_rate']
#         else:
#             i['last_rate'] = 5
#             i['points'] += i['last_rate']
#     for i in students:
#        ( print(i))
# cheker()
# Функция которая удаляет студента
#
def car(**kwargs):
    return kwargs
print(car(mark = 'Mersedec-Benz', model = 'w212', color = 'white' ))
# ** = Словарь


# Позиционный аргунмент
# Именованный аргумент
#  def plus(a, b=2, *args):
#     return sum(args)* a + b
# print(plus(2, 3, 4, 5))

# def plus(*args):
#     return sum(args)
# print(plus(2, 3, 4, 5, 7))

# звездечка помогает преобррразовать какойто обьект в кортедж


# def plus(a, b):
#     return a + b
# c = (plus(5, 10))
# print(c)
# print(plus(2, 3))



# def plus(a, b, c):
#     return a + b + c
# print(plus(5, 2, 3))



# name = ' jack'
# name1 = 'anna'
# print('hello', name)
# print('hello', name1)
# Функция def

# def greeting(name= 'Rick'):
#     print('hello', name)
# greeting('aman')
# greeting('amantur')
# greeting('Aza')
# greeting()

