from math import factorial

from Tools.scripts.generate_sre_constants import sre_constants_header

import math

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_hell(self):
#         print(f"Hello!My name is {self.name}")
#
#
#     def get_info(self):
#         return f"{self.name};{self.age}"
#
#
# vasya = Student("vasya", 15)
# petya = Student("petya", 17)
# anna = Student("anna", 111)
# print(vasya)
# print(vasya.age, vasya.name)
# print(petya.age, petya.name)
# print(anna.age, anna.name)
# vasya.say_hell()
# print(vasya.get_info())
#
# del vasya




# class Animal:
#     animal_counter = 0
#     def __init__(self, animal_type, name):
#         self.animal_type = animal_type
#         self.name = name
#         Animal.animal_counter += 1
#
#     def show_info(self):
#         print(f"{self.animal_type};{self.name}")
#
#
# barsik = Animal("Cat", "Barsik")
# bobik = Animal("dog", "Bobik")
# barsik.show_info()
# print(Animal.animal_counter)
# print(bobik.animal_counter)
# print(barsik.animal_counter)



# class Weather:
#     @staticmethod
#     def celsium_to_farenheit(t):
#         return t * 9/5 + 32
#
#     @staticmethod
#     def celsium_to_kelvin(t):
#         return t + 273.15
#
#     def farenheit_to_celsium(t):
#         return (t - 32) * 5/9
#
#     @staticmethod
#     def farenheit_to_kelvins(t):
#         return (t - 32) * 5/9 + 273.15
#
#     @staticmethod
#     def kelvin_to_celsium(t):
#         return t - 273.15
#
#     @staticmethod
#     def kelvin_to_farenheit(t):
#         return (t - 273.15) * 9/5 + 32
#
#
#
# print(Weather.celsium_to_farenheit(2))
# print(Weather.celsium_to_kelvin(0))
# print(Weather.farenheit_to_celsium(0))
# print(Weather.farenheit_to_kelvins(0))
# print(Weather.kelvin_to_celsium(0))
# print(Weather.kelvin_to_farenheit(0))




# class Fraction:
#     def __init__(self, numerator,denumenator):
#         self.a = numerator
#         self.b = denumenator
#         self.reduction()
#
#     def __str__(self):
#         return f"{self.a}/{self.b}"
#
#     def multiplication(self, other):
#         return Fraction(self.a * other.a, self.b * other.b)
#
#     def division(self,other):
#         return Fraction(self.a * other.b, self.b * other.a)
#
#     def __add__(self, other):
#         return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)
#
#     def __sub__(self, other):
#         return Fraction(self.a * other.b - self.b * other.a, self.a * other.b)
#
#     def __mul__(self, other):
#         return Fraction(self.a * other.a, self.b * other.b)
#
#     def __truediv__(self, other):
#         return Fraction(self.a * other.b, self.b * other.a)
#
#     def __iadd__(self, other):
#         self.a = self.a * other.b + self.b*other.a
#         self.b = self.b * other.b
#         return self
#
#     def __isub__(self, other):
#         self.a = self.a * other.b - self.b*other.a
#         self.b = self.b * other.b
#         return self
#
#     def __imul__(self, other):
#         self.a = self.a * other.a
#         self.b = self.b * other.b
#         return self
#
#     def __itruediv__(self, other):
#         self.a, self.b = self.a * other.b, self.b * other.a
#         return self
#     def __gt__(self,other):
#         return self.a * other.b > self.b * other.a
#
#     def __lt__(self, other):
#         return self.a * other.b < self.b * other.a
#
#     def __eq__(self, other):
#         return self.a * other.b == self.b * other.a
#
#     def __ne__(self, other):
#         return self.a * other.b != self.b * other.a
#
#     def __ge__(self, other):
#         return self.a * other.b >= self.b * other.a
#
#     def __le__(self, other):
#         return self.a * other.b <= self.b * other.a
#
#     def reduction(self):
#         common_divider = math.gcd(self.a, self.b)
#         self.a = self.a // common_divider
#         self.b = self.b // common_divider
#
#
#
#
# first = Fraction(2, 5)
# print(first)
# second = Fraction(2, 3)
# print(first.multiplication(second))
# print(first.division(second))
# print(first + second)
# print(first - second)
# print(first * second)
# print(first / second)
# first += second
# print(first)
# first -= second
# print(first)
# print(first > second)
#
#
# print(Fraction(50, 100) * (Fraction(2, 2)))
# import math
# class MyMath:
#
#     @staticmethod
#     def max_of_four(a, b, c, d):
#         return max(a, b, c, d)
#
#     @staticmethod
#     def min_of_four(a, b, c, d):
#         return min(a, b, c, d)
#
#     @staticmethod
#     def avg_of_four(a, b, c, d):
#         return f"{(a + b + c + d)/4}"
#
#     @staticmethod
#     def factorial(n):
#         math.factorial(4)

# from abc import ABC, abstractmethod
#
#
# class Figure2D(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#
#
# class Square(Figure2D):
#     def __init__(self, side):
#         self.side = side
#
#     def area_sq(self, side):
#         return side ** 2
#
#     def pirimeter_sq(self, side):
#         return self.side * 4
#
# sponge_bob = Square(5)
# sponge_bob.area_sq(66)


















