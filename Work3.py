a = int(input('Введите номер месяца - '))
while int(a) < 0:
    print('Месяц не может быть отрицательным!')
    a = int(input('Введите номер месяца - '))
while int(a) > 13:
    print('В году 12 месяцев, введите число до 13!')
    a = int(input('Введите номер месяца - '))
new_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}
print(new_dict.setdefault(a))
