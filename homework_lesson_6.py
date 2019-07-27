from math import pi
import random as R

#                                               Задание 1:
print('Задание 1: ')
print()
# Определите класс Apple с четырьмя переменными экземпляра, представляющими четыре свойства яблока.


class Apple:
    def __init__(self, v, c, w, s):
        self.view = v
        self.color = c
        self.weight = w
        self.size = s


ap1 = Apple('Antonovka', 'White Green', 200, 'Small')
ap2 = Apple('GoldenDel', 'Green', 180, 'Small')
ap3 = Apple('Melba', 'Red', 340, 'Big')

print(f"Sort: {ap1.view}, Color: {ap1.color}, Weight: {ap1.weight} gramm")
print(f"Sort: {ap2.view}, Color: {ap2.color}, Weight: {ap2.weight} gramm")
print(f"Sort: {ap3.view}, Color: {ap3.color}, Weight: {ap3.weight} gramm")

print('__ __ __ __ __')
print()
#                                               Задание 2:
print('Задание 2: ')
print()
# Создайте класс Circle с методом area, подсчитывающим и возвращающим площадь круга. Затем создайте объект Circle,
# вызовите в нем метод area и выведите результат. Воспользуйтесь функцией pi из встроенного в Python модуля math.


class Circle:
    def __init__(self):
        self.square = 0

    def area(self, r):
        self.square = pi * (r ** 2)


radius = R.randint(2, 10)
cir = Circle()
cir.area(radius)
print(f"We have circle: R = {radius}, S: {round(cir.square, 2)}")

print('__ __ __ __ __')
print()
#                                               Задание 3:
print('Задание 3: ')
print()
# Есть класс Person, конструктор которого принимает три параметра (не учитывая self) –
# имя, фамилию и квалификацию специалиста. Квалификация имеет значение заданное по умолчанию, равное единице.


class Person:
    def __init__(self, fn, n, q=1):
     self.name = n
     self.firstname = fn
     self.qualification = q

#                                               Задание 3(2):
# У класса Person есть метод, который возвращает строку, включающую в себя всю информацию о сотруднике.
    def perinfo(self, Person):
        print(f" Сотрудник: {Person.firstname} {Person.name}, имеет квалификацию: {Person.qualification}.")

pr1, pr2, pr3 = Person('Пайташ', 'Алексей', 'Junior Develop'), Person('Пайташ', 'Марина', 'Director, ИП Пайташ'), Person('Караленя', 'Юрий', 'Машинист сборочной линии')
pr1.perinfo(pr1)
pr2.perinfo(pr2)
pr3.perinfo(pr3)

print('__ __ __ __ __')
print()
#                                               Задание 4:
print('Задание 4: ')
print()
# Создайте класс Triangle с методом area, подсчитывающим и возвращающим площадь треугольника.
# Затем создайте объект Triangle, вызовите в нем area и выведите результат
class Triangle:
    def __init__(self):
        self.square = 0

    def area(self, a, h):
        self.square =  0.5 * (a * h)


side = R.randint(2, 10)
height = R.randint(2, 8)
tri = Triangle()
tri.area(side, height)
print(f"We have triangle: Side = {side}, Height = {height}, S: {round(tri.square, 2)}")


print('__ __ __ __ __')
print()

#                                               Задание 5:
print('Задание 5: ')
print()
# Создайте классы Rectangle и Square с методом calculate_perimeter, вычисляющим периметр фигур,
# которые эти классы представляют. Создайте объекты Rectangle и Square вызовите в них этот метод.
class Rectangle:
    def __init__(self):
        self.perimetr = 0

    def calculate_perimetr(self, a, b):
        self.perimetr = 2 * (a + b)


class Square:
    def __init__(self):
        self.perimetr = 0

    def calculate_perimetr(self, a):
        self.perimetr = 4 * a

    def change_size(self, i):
        self.newside = i

st1 = R.randint(2, 10)
st2 = R.randint(2, 10)
sq1 = R.randint(2, 10)
Re = Rectangle()
Re.calculate_perimetr(st1, st2)
Sq = Square()
Sq.calculate_perimetr(sq1)
print(f"We have Rectangle: Side №1 = {st1}, Side №2 = {st2}, Perimetr: {Re.perimetr}")
print(f"We have Squere: Side = {sq1}, Perimetr: {Sq.perimetr}")

#                                               Задание 6:
# В классе Square определите метод change_size, позволяющий передавать ему число, которое увеличивает или
# уменьшает (если оно отрицательное) каждую сторону объекта Square на соответствующее значение
sq2 = int(input('На какое число Вы хотите изменить сторону квадрата? '))
Sq.change_size(sq2)
Sq.calculate_perimetr(sq1 - sq2)
print(f"We have New Squere: New Side = {sq1 - sq2}, Perimetr: {Sq.perimetr}")