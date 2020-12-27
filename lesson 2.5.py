my_list = [7, 5, 3, 3, 2]
print(f"Текущий рейтинг - {my_list}")
number = int(input(f"Введите следующее значение, для выхода введите - '00': "))
while number != 00:
    for el in range(len(my_list)):
        if my_list[el] == number:
            my_list.insert(el + 1, number)
            break
        elif my_list[0] < number:
            my_list.insert(0, number)
        elif my_list[-1] > number:
            my_list.append(number)
        elif my_list[el] > number and my_list[el + 1] < number:
            my_list.insert(el + 1, number)
    print(f"текущий рейтинг - {my_list}")
    number = int(input("Введите следующее значение, для выхода введите - '00': "))
if number == 00:
    print(f"Итоговый рейтинг - {my_list}")
