import simple_draw as sd

coordinates_of_snowflakes_x = []
coordinates_of_snowflakes_y = []
snowflakes_length = []




def create_snowflakes(quantity):

    for i in range(0, quantity):
        coordinates_of_snowflakes_x.append(sd.random_number(0, sd.resolution[0]))
        coordinates_of_snowflakes_y.append(sd.random_number(sd.resolution[1], sd.resolution[1] + 600))
        snowflakes_length.append(sd.random_number(10, 30))


def draw_snowflakes_with_color(color=sd.background_color):

    for i in range(0, len(coordinates_of_snowflakes_y)):
        sd.start_drawing()
        point = sd.get_point(coordinates_of_snowflakes_x[i], coordinates_of_snowflakes_y[i])
        sd.snowflake(center=point, length=snowflakes_length[i], color=color)
        sd.finish_drawing()




def snowflake_shift(falling_speed=12):
    for i in range(0, len(coordinates_of_snowflakes_y)):
        coordinates_of_snowflakes_x[i] += sd.random_number(-25, 25)
        coordinates_of_snowflakes_y[i] -= falling_speed


def numbers_reached_bottom_of_screen():
    numbers_of_snowflakes_that_have_reached_the_end = []
    for i in range(0, len(coordinates_of_snowflakes_y)):
        if coordinates_of_snowflakes_y[i] <= 0:
            numbers_of_snowflakes_that_have_reached_the_end.append(i)
    return numbers_of_snowflakes_that_have_reached_the_end

def remove_snowflakes(col):

    for i in range(0, len(coordinates_of_snowflakes_y)-col):
        if coordinates_of_snowflakes_y[i] <= 0:
            coordinates_of_snowflakes_x.pop(i)
            coordinates_of_snowflakes_y.pop(i)
            snowflakes_length.pop(i)

    # for i in number_list:
    #     coordinates_of_snowflakes_x.pop(i)
    #     coordinates_of_snowflakes_y.pop(i)
    #     snowflakes_length.pop(i)


