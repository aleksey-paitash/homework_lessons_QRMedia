# HomeWork for Lesson №5

print('Задание №1:')
# Задание №1:
# Условие:
# Создадим пустую функцию которая ничего не возвращает.
print('Создадим пустую функцию которая ничего не возвращает')


def func():
    pass


print('Created!')

print('__ __ __ __ __ __ __')
print('Задание №2:')
# Задание №2:
# Условие:
# Написать функцию, которая принимает число, возвращает его значение умноженное на два.

a = int(3)  # - временно, без ввода числа


def doubl(a):
    return a * 2


# print('a =', doubl(int(input('Введите число а = '))))     # - временно, без ввода числа
print('a=', doubl(a))  # - временно, без ввода числа

print('__ __ __ __ __ __ __')
print('Задание №3:')
# Задание №3:
# Условие:
# Напишем функцию, которая определяет параметр на чётность. Если чётное число принтим (‘yes’)
# в ином случае (‘no’).

c = int(3)


def chet(c):
    if c % 2 == 0:
        return 'YES'
    else:
        return 'NO'


print(chet(c))
print(chet(c + 1))

print('__ __ __ __ __ __ __')
print('Задание №4:')


# Задание №4:
# Условие:
# Пишем функцию, принимающую два аргумента. После чего проверим, если первое число больше 10,
# принтим (‘да’). Если меньше(‘нет’).

def doubl_sravn(a, b):
    if a > 10:
        return 'Да'
    else:
        return 'Нет'


print(doubl_sravn(7, 27))
print(doubl_sravn(12, 4))

print('__ __ __ __ __ __ __')
print('Задание №5:')
# Задание №5:
# Условие:
# Написать лямбда функцию, которая делит по модулю(%) два аргумента.

f = lambda x, y: x % y

print(f(6, 2))
print(f(8, 3))
print(f(7, 2))

print('__ __ __ __ __ __ __')
print('Задание №6:')


# Задание №6:
# Условие:
# Создадим функцию с простыми командами. Обернём её в декоратор, который бы дополнял возможности функции.

def new1(arnament1):
    def new2():
        print('=(0)= =(*)=')
        arnament1()
        print('=(*)= =(0)=')

    return new2


@new1
def for_me():
    print('== =(*)= ==')


for_me()
print()
print('* - Win!!!')

print('__ __ __ __ __ __ __')
print('Задание №7:')
# Задание №7:
# Условие:
# Использовать функцию map и filter

number = [1, 2, 3, 5, 8, 13, 21]


def matemat1(i):
    return i ** 2


def matemat2(i):
    return i % 2 != 0


result1 = list(map(matemat1, number))
print(result1)
result2 = list(filter(matemat2, number))
print(result2)

print('__ __ __ __ __ __ __')
print('Задание №8:')
# Задание №8:
# Условие:
# Создадим чистую и нечистую функцию.
print('Чистая функция:')


def clean(a, b):
    return a ** b


print(clean(2, 4))

print('Нечистая функция:')


def no_clean(clean, a, b):
    return clean(clean(a, b), clean(a, b))


print(no_clean(clean, 2, 2))

print('__ __ __ __ __ __ __')
print('Задание №9:')
# Задание №9:
# Условие:
# Сделать функцию поиска минимума и максимума в списке.
numb = [43, 76, 8, 52, 15]


def m_m(numb):
    print('max =', max(numb), 'min =', min(numb))


m_m(numb)

print('__ __ __ __ __ __ __')
print('Задание №10:')
# Задание №10:
# Условие:
# Написать функцию, которая определяет, является ли год високосным.
# Пользователь вводит год, если он високосный, то функция
# возвращает True. Если нет, то False.
import calendar


def vis(god):
    print(calendar.isleap(god))


vis(2019)
# vis(int(input()))

print('__ __ __ __ __ __ __')
print('Задание №11:')


# Задание №11:
# Условие:
# Написать функцию season, принимающую 1 аргумент — номер месяца
# (от 1 до 12), и возвращающую время года, которому этот месяц
# принадлежит (зима, весна, лето или осень).

def season(i):
    if i in range(1, 3) or i == 12:
        return 'Winter'
    if i in range(3, 6):
        return 'Spring'
    if i in range(6, 9):
        return 'Summer'
    if i in range(9, 12):
        return 'Autumn'
    else:
        return 'ERROR'


i = 8
# i = (int(input()))
print(season(i))

print('__ __ __ __ __ __ __')
print('Задание №12:')


# Задание №12:
# Условие:
# Написать функцию date, принимающую 3 аргумента — день, месяц и год.
# Вернуть True, если такая дата есть в нашем календаре, и
# False иначе.*

def date(year, month, day):
    year, month, day = day, month, year
    try:
        if calendar.weekday(year, month, day) != False or calendar.weekday(year, month, day) == 0:  # try - except - если выдает ошибку
            return 'TRUE'
    except:
        return 'FALSE'

print(date(28, 2, 1989))

print('__ __ __ __ __ __ __')
print('Задание №13:')
# Задание №13:
# Условие:
# Список [16, -17, 2, 78.7, False, False, {‘True’: True}, 555, 12,
# 23, 42, ‘DD’] Функция, принимает на вход список -выбирает из
# него все int и float -составить из него новый список,
# отсортированный от наименьшего значения большему.
