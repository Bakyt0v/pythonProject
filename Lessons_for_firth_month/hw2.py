def horoscope(day, month, name=name):
    name =
    if day >= 21 and month == 1 or day <= 19 and month == 2:
        print('Воделей')
    if day >= 20 and month == 2 or day <= 20 and month == 3:
       print('Рыбы')
    if day >= 21 and month == 3 or day <= 20 and month == 4:
        print("Овен")
    if day >= 21 and month == 4 or day <= 21 and month == 5:
        print("Телец")
    if day >= 22 and month == 5 or day <= 21 and month == 6:
        print("Близнецы")
    if day >= 22 and month == 6 or day <= 22 and month == 7:
        print("Рак")
    if day >= 23 and month == 7 or day <= 21 and month == 8:
        print("Лев")
    if day >= 22 and month == 8 or day <= 23 and month == 9:
        print("Дева")
    if day >= 24 and month == 9 or day <= 23 and month == 10:
        print("Весы")
    if day >= 24 and month == 10 or day <= 23 and month == 11:
        print("Скорпион")
    if day >= 24 and month == 11 or day <= 22 and month == 12:
        print("Стрелец")
    if day >= 23 and month == 12 or day <= 20 and month == 1:
        print("Козерог")
    return
a = int(input('Enter the date:'))
b = int(input('Enter the month:'))
n = input('Enter the Name:')
print(horoscope(a, b, n))