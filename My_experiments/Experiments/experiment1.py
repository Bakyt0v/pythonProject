list1 = ['1','2','3','4']
list2 = ['23','12','33','45']
list3 = ['3','22','43','64']



copy_list = list1.copy()
list1.extend(copy_list)
print(list1)