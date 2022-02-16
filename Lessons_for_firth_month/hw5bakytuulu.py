# Первое задание задача (а)
def rectangle(height, width):
    return float(height * width)
print(f'Площадь прямоугольника ровняется:', rectangle(5, 5))



# Первое задание задача (b)
def infinity(a, *args):
    return int(sum(args)/a)
print(f'Среднее арифметическое число фунции infinity:',infinity(5, 2, 4, 6, 8, 10))



# Первое задание задача (c)
def menu(**kwargs):
    print(kwargs)
    return
menu(breakfast = 'rise')
menu(lunch='friedchicken')
menu(dinner='plov')
print(menu())
