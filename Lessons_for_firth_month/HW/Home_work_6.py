ten = list(range(1, 11))
evens = list(filter(lambda x: x % 2 == 0, ten))
square = list(map(lambda x: x * x, evens))
print('Список ten:', ten)
print('Список evens:', evens)
print('Возведенные в квадрат числа от списка evens:', square)

def text_index(x):
 try:
     return ten[x]
 except IndexError:
     return 'Введите Index 0 до', len(ten) -1

while True:
    a1 = input('Введите индекc:(Введите число 10 для выхода): ')
    if a1 == "10":
        break
    else:
        try:
            print(text_index(int(a1)))
        except ValueError:
            print('Введите только цифры от 0 до', len(ten) -1)