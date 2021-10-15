# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1300, 700)

def draw_branches(point, angle, length):
    if length < 10:
        return

    v1 = sd.get_vector(start_point=point, angle=angle-(30 + sd.random_number(-30, 30)/100), length=length, width=1)
    v1.draw()
    v2 = sd.get_vector(start_point=point, angle=angle+(30 + sd.random_number(-30, 30)/100), length=length, width=1)
    v2.draw()
    next_point_1 = v1.end_point
    next_angle_1 = angle - (30 + 30 * sd.random_number(-40, 40)/100)
    next_length = length * (.75 + .75 * sd.random_number(-20, 20)/100)
    draw_branches(point=next_point_1, angle=next_angle_1, length=next_length)
    next_point_2 = v2.end_point
    next_angle_2 = angle + (30 + 30 * sd.random_number(-40, 40)/100)
    next_length_2 = length * (.75 + .75 * sd.random_number(-20, 20)/100)
    draw_branches(point=next_point_2, angle=next_angle_2, length=next_length_2)


point_0 = sd.get_point(600, 10)
draw_branches(point=point_0, angle=90, length=75)


sd.pause()


