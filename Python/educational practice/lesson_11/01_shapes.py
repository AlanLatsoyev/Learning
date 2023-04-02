# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def get_figures(point, angle, length, color=sd.COLOR_YELLOW, width=2):
        for _ in range(n):
            v_ = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
            v_.draw(color=color)
            point = v_.end_point
            angle += 360 / n

    return get_figures


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)

sd.pause()
