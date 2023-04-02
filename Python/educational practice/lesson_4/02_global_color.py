# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg
def figures(point, angle=0, length=100, number_of_corners=3, color=sd.COLOR_YELLOW, width=2):
    for _ in range(number_of_corners):
        v_ = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
        v_.draw(color=color)
        point = v_.end_point
        angle += 360 / number_of_corners


colors = {0: sd.COLOR_RED,
          1: sd.COLOR_ORANGE,
          2: sd.COLOR_YELLOW,
          3: sd.COLOR_GREEN,
          4: sd.COLOR_CYAN,
          5: sd.COLOR_BLUE,
          6: sd.COLOR_PURPLE
          }
print('''Возможные цвета 
         0: 'red',
         1: 'orange',
         2: 'yellow',
         3: 'green',
         4: 'cyan',
         5: 'blue',
         6: 'purple' ''')
_ = 1
while _ != 0:
    code_of_color = int(input('Введите номер желаемого цвета >'))
    if code_of_color in list(colors):
        color = colors[code_of_color]

        point_0 = sd.get_point(100, 100)
        figures(point=point_0, number_of_corners=3, color=color)

        point_0 = sd.get_point(100, 400)
        figures(point=point_0, number_of_corners=4, color=color)

        point_0 = sd.get_point(400, 100)
        figures(point=point_0, number_of_corners=5, color=color)

        point_0 = sd.get_point(400, 400)
        figures(point=point_0, number_of_corners=6, color=color)
        break
    else:
        print('Вы ввели некорректный номер')
        continue

sd.pause()
