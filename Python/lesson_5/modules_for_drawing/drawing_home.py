# -*- coding: utf-8 -*-
import simple_draw as sd


# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


def wall(point):
    x = point.x
    y = point.y
    start_x = x
    end_x = x + 200

    start_y = y
    end_y = y + 200

    for y in range(start_y, end_y, 5):

        for x in range(start_x, end_x, 10):
            start_point = sd.get_point(x, y)
            end_point = sd.get_point(x + 10, y)
            sd.line(start_point=start_point, end_point=end_point, width=1)
            if y // 5 % 2 > 0:
                x = x + 5
            start_point = sd.get_point(x, y)
            end_point = sd.get_point(x, y + 5)
            sd.line(start_point=start_point, end_point=end_point, width=1)
    point = sd.get_point(start_x, start_y)
    figures(point=point, length=200, number_of_corners=4, color=sd.COLOR_BLACK, width=2)


def figures(point, angle=0, length=100, number_of_corners=3, color=sd.COLOR_YELLOW, width=1):
    for _ in range(number_of_corners):
        v_ = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
        v_.draw(color=color)
        point = v_.end_point
        angle += 360 / number_of_corners


def windows(point, length=50, width=1):
    point.x = point.x + 75
    point.y = point.y + 75
    while length > 0:
        figures(point=point, length=length, number_of_corners=4, width=width, color=sd.COLOR_WHITE)
        length -= width
    point.x = point.x - 75
    point.y = point.y - 75


def roof(point, length=50, width=1):
    point.y = point.y + 200
    while length > 0:
        figures(point=point, length=length, number_of_corners=3, width=width, color=sd.COLOR_DARK_RED)
        length -= width
    point.y = point.y - 200


def home(point):
    roof(point=point, length=200)
    wall(point=point)
    windows(point=point)


point = sd.get_point(400, 100)
home(point=point)

sd.pause()
