new_list = [8, 6, 4, 4, 3, 2]
a = int(input('Введите новое натуральное число для рейтинга - '))
while int(a) < 0:
    print('Число должно быть натуральным!')
    a = int(input('Введите новое натуральное число для рейтинга - '))
new_list.append(a)
new_list.sort(reverse = True)
print(new_list)