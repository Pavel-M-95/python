user_answer = int(input('Введите номер месяца: '))
seasons_list = ['зима', ' весна', 'лето', 'осень']
seasons_dict = {1: 'зима', 2: ' весна', 3: 'лето', 4: 'осень'}
if user_answer == 1 or user_answer == 2 or user_answer == 12:
    print('Это: ' + seasons_list[0])
    print('Это: ' + seasons_dict.get(1))

elif user_answer == 3 or user_answer == 4 or user_answer ==  5:
    print('Это: ' + seasons_list[1])
    print('Это: ' + seasons_dict.get(2))
elif user_answer == 6 or user_answer == 7 or user_answer == 8:
    print('Это: ' + seasons_list[2])
    print('Это: ' + seasons_dict.get(3))

elif user_answer == 9 or user_answer == 10 or user_answer == 11:
    print('Это: ' + seasons_list[2])
    print('Это: ' + seasons_dict.get(3))
elif user_answer > 12:
    print('Такого месяца не существует')






