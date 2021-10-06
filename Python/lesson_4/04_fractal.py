# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1300, 700)
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# def draw_branches(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle-30, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=point, angle=angle+30, length=length, width=3)
#     v2.draw()


# def draw_branches(point, angle, length, delta):
#     if length < 10:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle-delta, length=length, width=1)
#     v1.draw()
#     v2 = sd.get_vector(start_point=point, angle=angle+delta, length=length, width=1)
#     v2.draw()
#     next_point_1 = v1.end_point
#     next_point_2 = v2.end_point
#     next_angle_1 = angle - delta
#     next_angle_2 = angle + delta
#     next_length_1 = length * .75
#     next_length_2 = length * .75
#     draw_branches(point=next_point_1, angle=next_angle_1, length=next_length_1, delta=delta)
#     draw_branches(point=next_point_2, angle=next_angle_2, length=next_length_2, delta=delta)
#
#
# point_0 = sd.get_point(600, 10)
# draw_branches(point=point_0, angle=90, length=100, delta=30)



# def branch(point, angle, length, delta):
#     if length < 1:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     next_point = v1.end_point
#     next_angle = angle - delta
#     next_length = length * .75
#     branch(point=next_point, angle=next_angle, length=next_length, delta=delta)
# TODO здесь ваш код

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# delta_angle = sd.random_number(18, 42)
# delta_length = sd.random_number(.6, .9)
def draw_branches(point, angle, length):
    if length < 10:
        return

    v1 = sd.get_vector(start_point=point, angle=angle-(30 + sd.random_number(-30, 30)/100), length=length, width=1)
    v1.draw()
    next_point_1 = v1.end_point
    next_angle_1 = angle - (30 + 30 * sd.random_number(-40, 40)/100)
    next_length = length * (.75 + .75 * sd.random_number(-20, 20)/100)
    draw_branches(point=next_point_1, angle=next_angle_1, length=next_length)


    v2 = sd.get_vector(start_point=point, angle=angle+(30 + sd.random_number(-30, 30)/100), length=length, width=1)
    v2.draw()
    next_point_2 = v2.end_point
    next_angle_2 = angle + (30 + 30 * sd.random_number(-40, 40)/100)
    next_length_2 = length * (.75 + .75 * sd.random_number(-20, 20)/100)
    draw_branches(point=next_point_2, angle=next_angle_2, length=next_length_2)


point_0 = sd.get_point(600, 10)
draw_branches(point=point_0, angle=90, length=100)


sd.pause()


