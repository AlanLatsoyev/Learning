# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall
from lesson_6.snowfall import create_snowflakes, draw_snowflakes_with_color, snowflake_shift, \
    remove_snowflakes, numbers_reached_bottom_of_screen, \
    coordinates_of_snowflakes_x, coordinates_of_snowflakes_y

# создать_снежинки(N)
n = 100
create_snowflakes(quantity=n)

while True:
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    draw_snowflakes_with_color(color=sd.background_color)
    #  сдвинуть_снежинки()

    snowflake_shift(falling_speed=10)
    # print(len(numbers_reached_bottom_of_screen()))
    #  нарисовать_снежинки_цветом(color)
    draw_snowflakes_with_color(color=sd.COLOR_WHITE)
    #  если есть номера_достигших_низа_экрана() то

    # print(coordinates_of_snowflakes_y)
    # print(coordinates_of_snowflakes_x)
    number_list = numbers_reached_bottom_of_screen()

    if number_list != []:
        #       удалить_снежинки(номера)
        remove_snowflakes(col=len(number_list))
        # print(len(numbers_reached_bottom_of_screen()))
        #       создать_снежинки(count)
        create_snowflakes(quantity=n - len(coordinates_of_snowflakes_y))

    sd.sleep(0.2)
    if sd.user_want_exit():
        break

sd.pause()
