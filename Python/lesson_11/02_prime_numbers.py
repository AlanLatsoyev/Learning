# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел
from math import sqrt


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    def __init__(self, n):
        self.i = 0
        self.n = n
        self.list_prime_nambers = []

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.n:
            raise StopIteration
        if self.i > 1:
            if not [x for x in self.list_prime_nambers if self.i % x == 0]:
                self.list_prime_nambers.append(self.i)
                return self.i
        return self.__next__()


prime_number_iterator = PrimeNumbers(n=10000)
for number in prime_number_iterator:
    print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик
def heppy_filter(number):
    str_number = [x for x in str(number)]
    quantity = len(str_number)
    half_line = quantity // 2
    if quantity > 1 :
        if quantity % 2 == 0:
            if str_number[:half_line] == str_number[half_line:]:
                return True
        else:
            if int(str_number[half_line]) % 2 == 0 or int(str_number[half_line]) == 0:
                if str_number[:half_line] == str_number[half_line + 1:]:
                    return True
    return False


def palindrome_filter(number):
    str_number = str(number)
    if len(str_number) > 1:
        if str_number == str_number[::-1]:
            return True
    return False


def prime_numbers_generator(n):
    if 2 <= n:
        yield 2
    yield from (
        i
        for i in range(3, n + 1, 2)
        if all(i % x != 0 for x in range(3, int(sqrt(i) + 1)))
    )

prime_numbers_list = []
for number in prime_numbers_generator(n=100000):
    print(number)
    prime_numbers_list.append(number)
print(f'{len(prime_numbers_list)}')
print(f'{list(filter(heppy_filter, prime_numbers_list))} - числа счастливые \n'
      f'{list(filter(palindrome_filter, prime_numbers_list))} - числа зеркальные')

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
