goods = []
features = {'Название': '', 'Цена': '', 'Количество': '', 'ед': ''}
analytics = {'Название': [], 'Цена': [], 'Количество': [], 'ед': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода введите 'Q',\nдля внесения даных нажмите 'Enter',\nдля вывода информации о товаре нажмите 'F'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'F':
        print(f'\nИнформация о товаре:\n')
        for key, value in analytics.items():
            print('-'*50 + f'\n{key:>10}: {value}')
    for f in features.keys():
        feature_ = input(f'Введите данные о товаре "{f}": ')
        features[f] = int(feature_) if (f == 'Цена' or f == 'Количество') else feature_
        analytics[f].append(features[f])
        goods.append((num, features))
