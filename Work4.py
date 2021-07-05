a = str(input('Введите несколько слов - '))
a = list(a.split())
i = 1
b = 0
for el in a:
    if len(el) > 10:
        print(i, a[b][0:10])
        i += 1
        b += 1
    else:
        print(i, a[b])
        i += 1
        b += 1





