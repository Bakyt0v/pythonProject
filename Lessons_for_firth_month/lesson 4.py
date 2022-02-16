car = dict(brand='BMW', model='e34', color='black')
# буква к ключ key букваа v значение value
# items отображает кдюч и значение сразу
car.update(year=1995)
for k, v in car.items():
    print(f'{k}: {v}:')
car2 = car.copy()
car2['color'] = 'silver'
print(car)
print(car2)
print(car.get('obem', 'нет такого'))
print(car.get('model'))
print(car.keys())
print(car.values())
#
ключом пишется строчка ключ это слово в ковычках
СОЗДАНИЕ СЛОВАРЯ
# student = {
#     'name': 'Argen',
    'age': 20,
    'skills': ['english', 'programming'],
    'bad habbits': 'smoking',
}
# Изменение словаря
student['gender'] = 'male'
student['age'] = 21
del student['bad habbits']
# student.update(car)
print(student)

