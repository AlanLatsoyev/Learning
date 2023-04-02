# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint

class IamGodError(Exception):
    pass
class DrunkError(Exception):
    pass
class CarCrashError(Exception):
    pass
class GluttonyError(Exception):
    pass
class DepressionError(Exception):
    pass
class SuicideError(Exception):
    pass

def one_day():
    karma = randint(1, 14)
    if karma in range(1, 8):
        return karma
    elif karma == 8:
        raise IamGodError('возомнил себя Богом !')
    elif karma == 9:
        raise DrunkError('перепил!')
    elif karma == 10:
        raise CarCrashError('попал в автокатастрофу!')
    elif karma == 11:
        raise GluttonyError('переел!')
    elif karma == 12:
        raise DepressionError('депрессия одолела!')
    elif karma == 13:
        raise SuicideError('самоубился!')
    return 0






ENLIGHTENMENT_CARMA_LEVEL = 777
karma = 0
while karma < ENLIGHTENMENT_CARMA_LEVEL:
    try:
        karma += one_day()
    except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as exc:
        print(f'Сегодня день плохой {exc}')
    print(karma)

# https://goo.gl/JnsDqu
