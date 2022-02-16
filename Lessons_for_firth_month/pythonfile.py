# # name = input("what's your name?")
# # age = input('how old are you')
# # print(f' Your name {name}, you are {age} years old')
# # name = input(" what's your name: ")
# # year = input("What's your birth date: ")
#  print(f'Your name is {name}, you are {2021 - int(year)} years old')
def text_index(x):
 try:
     return ten[x]
 except IndexError:
     return 'введите только цифры ', len(ten)

ten = list(range(1, 11))
while True:
 a1 = input('введите индекс(введите "стоп" для завершения работы): ')
 if a1 == "стоп":
     break
 else:
     try:
         print(text_index(int(a1)))
     except ValueError:
         print('введите индекс от 0 до ', len(ten))