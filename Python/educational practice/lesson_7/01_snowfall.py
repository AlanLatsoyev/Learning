# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self):
        self.coordinate_x = sd.random_number(0, sd.resolution[0])
        self.coordinate_y = sd.random_number(sd.resolution[1], sd.resolution[1] + 800)
        self.snowflake_length = sd.random_number(10, 30)
        self.color = sd.COLOR_WHITE

    def snowflake_move(self):
        self.coordinate_x += sd.random_number(-25, 25)
        self.coordinate_y -= 15

    def snowflake_draw(self):
        sd.start_drawing()
        point = sd.get_point(self.coordinate_x, self.coordinate_y)
        sd.snowflake(center=point, length=self.snowflake_length, color=self.color)
        sd.finish_drawing()

    def clear_previous_picture(self):
        sd.start_drawing()
        point = sd.get_point(self.coordinate_x, self.coordinate_y)
        sd.snowflake(center=point, length=self.snowflake_length, color=sd.background_color)
        sd.finish_drawing()

    # def can_fall(self):
    #     if self.coordinate_y > 0 - self.snowflake_length:
    #
    #         return True




def get_flakes(count):
    list_flakes = []
    for snowflake in range(0, count):
        snowflake = Snowflake()
        list_flakes.append(snowflake)
    return list_flakes


def get_fallen_flakes():
    number_of_fallen_snowflakes = 0
    for flake in flakes:
        # if not flake.can_fall():
        #     number_of_fallen_snowflakes += 1
        if flake.coordinate_y < 0 - flake.snowflake_length:
            number_of_fallen_snowflakes += 1
            flakes.remove(flake)

    return number_of_fallen_snowflakes


def append_flakes(count):
    for snowflake in range(0, count):
        snowflake = Snowflake()
        flakes.append(snowflake)


# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.snowflake_move()
#     flake.snowflake_draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:

N = 200
sd.resolution = (1300, 700)

flakes = get_flakes(count=N)  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.snowflake_move()
        flake.snowflake_draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes != 0:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    # fallen_flakes = 0
    # for flake in flakes:
    #     print(flake.coordinate_y)
    #
    # print(len(flakes))
    # print(fallen_flakes)
    sd.sleep(0.0001)
    if sd.user_want_exit():
        break

sd.pause()
