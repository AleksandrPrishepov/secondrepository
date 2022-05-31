# a = input().split()
#
# for i in a:
#     if a.count(i) == 1:
#         print(i)







# d1 = tuple(int(i) for i in input().split())
# print(d1)
# d2 = tuple(int(i) for i in input().split())
# print(d2)
# if sum(d1) > sum(d2):
#     print(f'сумма больше в кортеже{d1}')
# elif sum(d1) < sum(d2):
#     print(f'сумма больше в кортеже{d2}')

# d1 = tuple(int(i) for i in input().split())
# print(f'Индекс максимального элемента {d1.index(max(d1))}')

# s = input()
# d = {}
# k = []
# v = []
# for i in s:
#     k.append(i)
#     v.append(s.count(i))
# print(dict(zip(k,v)))

# d = {'пепперони': (10, 'теста и колбаса'),
#      'маргарита': (8, 'тесто и сыр'),
#      'мясная': (15, 'сосиски, колбаса и тесто')}
# a = input('Какая пицца вас интересует: ').lower()
# b = input('Чтобы вы хотели уточнить: ').lower()
# l = ['описание', 'цена']
# for i in d:
#     if b == l[0] and a == i:
#         print(f'пицца {i} {d[i][1]}')
#     if b == l[1] and a == i:
#         print(f'пицца {i} стоит {d[i][0]}')

# with open('file_name.txt') as f:
#     for line in f:
#         a = int(line.split()[-1])
#         if a > 4:
#             print(line)
# c = []
# with open('file_name.txt') as f:
#     for line in f:
#         a = int(line.split()[-1])
#         c.append(a)
# print(len(c))

# d = {'пепперони': (10, 800),
#      'маргарита': (8, 900),
#      'мясная': (15, 600)}
# pizza_buy = input('Какую пиццу Вы хотели бы приобрести: ')
# weight = int(input('Сколько пиццы Вам положить(грамм): '))
#
# for i in d:
#     if i == pizza_buy:
#         print(f'к оплате {d[i][0] * weight/100}')
#         print(f'пиццы {i} осталось {d[i][1] - weight}')
# print(d)

# # exam_6_1
# l1 = [int(i) for i in input().split()]
# l2 = [int(i) for i in input().split()]
# s = set(l1) - set(l2)
# print(len(s))
















