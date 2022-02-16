from random import randint as random
import time

with open('text.txt', 'a', encoding='utf-8') as f:
    num_end = int(input('ведите количество попыток: '))
    name = input('введите ваше имя : ')
    n = 0
    time_begin = time.time()

    while n < num_end:
        s1 = random(1,9)
        s2 = random(1,9)
        user_answer = int(input(f'{s1} * {s2} = '))
        print(answer := s1 * s2)
        if user_answer != answer:
            f.write(f'{s1} * {s2} = {user_answer} ({answer}) неправильно\n')
        else:
            f.write(f'{s1} * {s2} = {user_answer} ({answer}) правильно\n')
        n +=1
    time_end = time.time() - time_begin
    f.write(f'было попыток :{num_end}, потраченное времья : {round(time_end)} сек, имя:{name}')