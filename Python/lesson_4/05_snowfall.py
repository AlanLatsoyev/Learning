# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1050, 700)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
# y = 500
# x = 100
#
# y2 = 450
# x2 = 150
# while True:
#     sd.clear_screen()
#     point = sd.get_point(x, y)
#     sd.snowflake(center=point, length=50)
#     y -= 10
#     if y < 50:
#        break
#     x = x + 10
#
#     point2 = sd.get_point(x2, y2)
#     sd.snowflake(center=point2, length=30)
#     y2 -= 10
#     if y2 < 50:
#        break
#     x2 = x2 + 20
#
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# while True:
#
#     for i in range(0, 19, 1):
#         sd.start_drawing()
#         point = sd.get_point(list_x[i], list_y[i])
#         sd.snowflake(center=point, length=list_length[i], color=sd.background_color)
#         list_y[i] -= 5
#         list_x[i] += 5
#         point = sd.get_point(list_x[i], list_y[i])
#         sd.snowflake(center=point, length=list_length[i], color=sd.COLOR_WHITE)
#         if list_y[i] <= 5:
#             break
#         sd.finish_drawing()
#
#     sd.sleep(0.0001)
#     if sd.user_want_exit():
#         break
#
# sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
list_x = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
list_y = [1000, 800, 1400, 1200, 900, 1300, 750, 1400, 750, 1200, 850, 1000, 1100, 1500, 1300, 790, 890, 1100, 900, 910]
list_length = [30, 33, 34, 35, 25, 26, 15, 20, 22, 38, 28, 39, 29, 24, 23, 21, 27, 32, 21, 31]

while True:

    for i in range(20):
        if list_y[i] < 50:
            list_y[i] = 750
            continue
        sd.start_drawing()
        point = sd.get_point(list_x[i], list_y[i])
        sd.snowflake(center=point, length=list_length[i], color=sd.background_color)
        list_y[i] -= 12
        list_x[i] += sd.random_number(-25, 25)
        point = sd.get_point(list_x[i], list_y[i])
        sd.snowflake(center=point, length=list_length[i], color=sd.COLOR_WHITE)

        sd.finish_drawing()

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
