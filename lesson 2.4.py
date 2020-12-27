my_word = input('Введите несколько слов в список: ')
my_list = []
num = 1
for i in range(my_word.count(' ') + 1):
    my_list = my_word.split(' ')
    if len(str(my_list)) <= 10:
        print(f" Номер {num} {my_list [i]}")
        num += 1
    else:
        print(f" Номер {num} {my_list[i] [0:10]}")
        num += 1
