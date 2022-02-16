a = list(map(int,input('Введите значения: ').split()))
odd = False
even = False
for i in a:
    if (i % 2 == 0):
        odd = True
    if i % 2 != 0:
        even = True
if odd and even:
    print('yes')
else:
    print('no')
