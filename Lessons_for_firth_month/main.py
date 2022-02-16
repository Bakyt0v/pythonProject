while True:
    word = input('Напишите любое слово: ')
    if word == ("стоп" or 'stop' or 'Stop' or 'Стоп'):
        break
    string = word
    count = 0
    list1 = "АУОИЕЮЫЯауоеиыюяAEUIOYayuioe"
    for i in string:
        if i in list1:
            count += 1
    print(f'Количество гласных букв:', count)
    countt = 0
    list2 = 'ЙЦКНГШЩЗХЪФВПРЛДЖЧСМТЬБQWRTPSDFGHJKLZXCVBNMйцкнгшщзхъфвпрлджчсмтьбqwrtpsdfghjklzxcvbnm'
    for i in string:
        if i in list2:
            countt +=1
    print('Количество согласных букв:', countt)
    r = 0
    sb = "АУОИЕЮЯауоеиюяAEUIOYayuioe"
    s = ' !@#$%^&*()":<>?| '
    for i in string:
        if i in sb or i not in sb and i in word and i not in s:
            r +=1
    print('Количество всех букв:',r)
    su1 = 0
    su = 'QWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
    for i in string:
        if i in su:
            su1 +=1;
    print('Количество Прописных букв:', su1)
    su2 = 0
    su0 = 'йцукенгшщзхъфывапролджэячсмитьбюqwertyuiopasdfghjklzxcvbnm'
    for i in string:
        if i in su0:
            su2 += 1;
    print('Количество строчных букв:', su2)
    t11 = round((100 / r) * count, 2)
    t12 = round((100 / r) * countt, 2)
    print('Гласные буквы/Согласные буквы:', t11,'% /',t12, "%")
