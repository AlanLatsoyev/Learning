# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)


start_x, end_x = 50, 350

for color in rainbow_colors:
    start_point = sd.get_point(start_x, 50)
    end_point = sd.get_point(end_x, 450)
    sd.line(start_point=start_point, end_point=end_point, color=color, width=4)
    start_x += 5
    end_x += 5
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

point = sd.get_point(400, -50)
radius = 500
for color in rainbow_colors:

    sd.circle(center_position=point, radius=radius, width=10, color=color)
    radius += 11
sd.pause()
