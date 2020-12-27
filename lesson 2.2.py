count = int(input('Введите требуемую длину списка: '))
my_list = []
i = 0
num = 1
j = 0
while i < count:
    my_list.append(input(f'Введите {num}-е число: '))
    i += 1
    num += 1
for i in range(int(len(my_list) / 2)):
    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    j += 2


print(my_list)


