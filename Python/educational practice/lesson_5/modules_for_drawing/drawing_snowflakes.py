import simple_draw as sd

sd.resolution = (1050, 700)




list_x = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
list_y = [1000, 800, 1400, 1200, 900, 1300, 750, 1400, 750, 1200, 850, 1000, 1100, 1500, 1300, 790, 890, 1100, 900, 910]
list_length = [30, 33, 34, 35, 25, 26, 15, 20, 22, 38, 28, 39, 29, 24, 23, 21, 27, 32, 21, 31]


def snowflkes():
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


snowflkes()

sd.pause()

