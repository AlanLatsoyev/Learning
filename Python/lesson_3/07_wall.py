# -*- coding: utf-8 -*-
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

for y in range(0, 1000, 50):



    for x in range(-50, 1000, 100):
        if y // 50 % 2 > 0:
            x = x + 50

        start_point = sd.get_point(x, y)
        end_point = sd.get_point(x+100, y)
        sd.line(start_point=start_point, end_point=end_point,  width=4)
        start_point = sd.get_point(x+100, y)
        end_point = sd.get_point(x + 100, y+50)
        sd.line(start_point=start_point, end_point=end_point, width=4)




sd.pause()
