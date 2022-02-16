from random import randint as random
import time
x = random(1, 100)
t = time.time()
tryes = 1
while True:
 try:
  num = int(input('введите число:'))
  if num > 100:
   print('вводите только числа от 1 до 100 !')
   continue
  else:
   if num != x:
    tryes +=1
    if num >= x - 5 and num <= x + 5:
     print("очень близко ", end='')
    elif num >= x - 10 and num <= x + 10:
     print("близко ", end='')
    if num > x:
     print('<')
    else:
     print('>')
   else:
    print('потрачено попыток: ', tryes)
    print('потрачено времемни:', round(time.time()-t),' секунд')
    break



 except ValueError:
  print('вводите только числа от 1 до 100 !')