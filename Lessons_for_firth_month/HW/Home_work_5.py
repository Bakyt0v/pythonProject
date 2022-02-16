def horoscope(day, month, name):
 if len(name) < 1:
   name = 'name'
 if day >= 21 and month == 1 or day <= 19 and month == 2:
  print(name,'Воделей')
 if day >= 20 and month == 2 or day <= 20 and month == 3:
  print(name,'Рыбы')
 if day >= 21 and month == 3 or day <= 20 and month == 4:
  print(name,"Овен")
 if day >= 21 and month == 4 or day <= 21 and month == 5:
  print(name,"Телец")
 if day >= 22 and month == 5 or day <= 21 and month == 6:
  print(name,"Близнецы")
 if day >= 22 and month == 6 or day <= 22 and month == 7:
  print(name,"Рак")
 if day >= 23 and month == 7 or day <= 21 and month == 8:
  print(name,"Лев")
 if day >= 22 and month == 8 or day <= 23 and month == 9:
  print(name,"Дева")
 if day >= 24 and month == 9 or day <= 23 and month == 10:
  print(name,"Весы")
 if day >= 24 and month == 10 or day <= 23 and month == 11:
  print(name,"Скорпион")
 if day >= 24 and month == 11 or day <= 22 and month == 12:
  print(name,"Стрелец")
 if day >= 23 and month == 12 or day <= 20 and month == 1:
  print(name,"Козерог")
 return

a = int(input('Enter the date:'))
b = int(input('Enter the month:'))
n = input('Enter the Name:')
print(horoscope(a, b, n))