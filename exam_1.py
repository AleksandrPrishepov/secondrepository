import random


# # exam_1_1
# num = int(input())
# num1 = str(num)
# event = 0
# odd = 0
# summ = 0
#
# while num > 0:
#     l_num = num % 10
#     if l_num % 2 == 0:
#         event += 1
#     else:
#         odd += 1
#     summ += l_num
#     num = num // 10
# print(event)
# print(odd)
# if event > odd:
#     print(f'Четных цифр больше, сумма цифр числа = {summ}')
# else:
#     multi = int(num1[5])*int(num1[2])*int(num1[0])
#     print(f'Нечетных цифр больше, произведение {num1[0]}, {num1[2]}, {num1[5]} = {multi}')
#
# # exam_1_2
# a = input().lower()
# vowels_str = 'aeiouy'
# vowels = 0
# consonants = 0
# l = []
#
# for i in a:
#     if i.isalpha() and i in vowels_str:
#         vowels += 1
#         l.append(i)
#     elif i.isalpha() and i not in vowels_str:
#         consonants += 1
# if vowels == consonants:
#     # for i in a:
#     #     if i in vowels_str:
#     #         print(i, end=' ')
#     print(*l)

# exam_1_3
# a_b_r1 = 0
# b_b_r2 = 0
# r2_iter_4 = 0
# r1_iter_4 = 0
# iter = 0
# for i in range(6):
#     iter += 1
#     a = int(input('Введите первое число: '))
#     b = int(input('Введите второе число: '))
#     r1 = random.randint(1, 20)
#     r2 = random.randint(1, 20)
#     print(r1)
#     print(r2)
#     if a > r1:
#         a_b_r1 += 1
#     if b > r2:
#         b_b_r2 += 1
#     if iter == 4:
#         r1_iter_4 = r1
#         r2_iter_4 = r2
# print(a_b_r1)
# print(b_b_r2)
# print(r1_iter_4)
# print(r2_iter_4)
# if a_b_r1 == b_b_r2:
#     print(f'Рандомные числа, полученные в 4ой итерации: {r1_iter_4}, {r2_iter_4}')

# # exam_1_4
# a = int(input("Коли-во рандомных чисел: "))
# b = int(input('Цифра которую исчим: '))
# n = 0
# for i in range(a):
#     r = random.randint(1,20)
#     print(r, end=' ')
#     while r > 0:
#         r_l = r % 10
#         if r_l == b:
#             n += 1
#         r = r // 10
# print()
# print(f'{b} встречается {n} раз')

# # exam_1_5
# a = input()
# n = 0
# for i in a:
#     if i.isdigit():
#         print(i, end=' ')

# # exam_1_6
# a = input()
# vowels_str = 'aeiouy'
# n_upper = 0
# n_lower = 0
# n_consontant = 0
# n_vowels = 0
# n_letters = 0
# for i in range(len(a)-1):
#     if a[i].isupper() and a[i+1].isupper():
#         n_upper += 1
#     if a[i].islower() and a[i+1].islower():
#         n_lower += 1
# for j in a.lower():
#     if j.isalpha() and j not in vowels_str:
#         n_consontant += 1
#     if j.isalpha() and j in vowels_str:
#         n_vowels += 1
#     if j.isalpha():
#         n_letters += 1
# print(f' Пар верхнего регистра: {n_upper}')
# print(f' Пар нижнего регистра: {n_lower}')
# print(f' гласные {n_vowels}')
# print(f' согласные {n_consontant}')
# print(f' всего букв {n_letters}')
























