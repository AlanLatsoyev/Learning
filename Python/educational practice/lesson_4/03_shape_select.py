# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def figures(point, angle=0, length=100, number_of_corners=3, color=sd.COLOR_YELLOW, width=2):
    for _ in range(number_of_corners):
        v_ = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
        v_.draw(color=color)
        point = v_.end_point
        angle += 360 / number_of_corners


all_figures = {0: 3,
               1: 4,
               2: 5,
               3: 6
               }
print('''Возможные фигуры
         0: 'треугольник',
         1: 'квадрат',
         2: 'пятиугольник',
         3: 'шестиугольник' ''')
_ = 1
while _ != 0:
    code_of_figure = int(input('Введите номер желаемой фигуры >'))
    if code_of_figure in list(all_figures):
        figure = all_figures[code_of_figure]
        point_0 = sd.get_point(300, 300)
        figures(point=point_0, number_of_corners=figure)
        break
    else:
        print('Вы ввели некорректный номер')
        continue
sd.pause()
