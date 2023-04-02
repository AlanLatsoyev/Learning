# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(x, y, color):
    left_bottom = sd.get_point(x - 50, y - 40)
    right_top = sd.get_point(x + 50, y + 40)
    sd.ellipse(left_bottom=left_bottom, right_top=right_top, width=2, color=color)
    point = sd.get_point(x - 20, y + 10)
    sd.circle(center_position=point, radius=4, width=0, color=color)
    point = sd.get_point(x + 20, y + 10)
    sd.circle(center_position=point, radius=4, width=0, color=color)
    point_list = [sd.get_point(x - 20, y - 20),
                  sd.get_point(x - 15, y - 25),
                  sd.get_point(x + 15, y - 25),
                  sd.get_point(x + 20, y - 20)]
    sd.lines(point_list=point_list, width=2, color=color)

for _ in range(10):
    smile(x=sd.random_number(a=0, b=600), y=sd.random_number(a=0, b=600), color=sd.random_color())

sd.pause()
