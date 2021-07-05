number = int(input('Введите номер товара - '))
name = str(input('Введите название товара - '))
price = int(input('Введите цену товара - '))
count = int(input('Введите количество товара - '))
number_1 = int(input('Введите номер товара - '))
name_1 = str(input('Введите название товара - '))
price_1 = int(input('Введите цену товара - '))
count_1 = int(input('Введите количество товара - '))
number_2 = int(input('Введите номер товара - '))
name_2 = str(input('Введите название товара - '))
price_2 = int(input('Введите цену товара - '))
count_2 = int(input('Введите количество товара - '))
main_list = [
    (number, {'Название': {name}, 'Цена': {price}, 'Количество': {count}, 'ед.': 'шт.'}),
    (number_1, {'Название': {name_1}, 'Цена': {price_1}, 'Количество': {count_1}, 'ед.': 'шт.'}),
    (number_2, {'Название': {name_2}, 'Цена': {price_2}, 'Количество': {count_2}, 'ед.': 'шт.'})
]
main_dict = {
'Название': [name, name_1, name_2],
'Цена': [price, price_1, price_2],
'Количество': [count, count_1, count_2],
'ед.': 'шт.'
}
print(main_list)
print(main_dict)