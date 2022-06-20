# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава
# Water + Air = Storm
# Water + Fire = Steam
# Water + Earth = Mud
# Air + Fire = Lightning
# Air + Earth = Dust
# Fire + Earth = Lava
# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if type(other) == Air:
            return Storm(part1=self, part2=other)
        elif type(other) == Fire:
            return Steam(part1=self, part2=other)
        elif type(other) == Earth:
            return Mud(part1=self, part2=other)


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if type(other) == Water:
            return Storm(part1=self, part2=other)
        elif type(other) == Fire:
            return Lightning(part1=self, part2=other)
        elif type(other) == Earth:
            return Dust(part1=self, part2=other)


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if type(other) == Air:
            return Lightning(part1=self, part2=other)
        elif type(other) == Water:
            return Steam(part1=self, part2=other)
        elif type(other) == Earth:
            return Lava(part1=self, part2=other)


class Earth:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if type(other) == Air:
            return Dust(part1=self, part2=other)
        elif type(other) == Fire:
            return Lava(part1=self, part2=other)
        elif type(other) == Water:
            return Mud(part1=self, part2=other)


class Storm:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Шторм. Состоит из ' + str(self.part1) + ' и ' + str(self.part2)


class Steam:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Пар. Состоит из ' + str(self.part1) + ' и ' + str(self.part2)


class Mud:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Грязь. Состоит из ' + str(self.part1) + ' и ' + str(self.part2)


class Lightning:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Молния. Состоит из ' + str(self.part1) + ' и ' + str(self.part2)


class Dust:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Пыль. Состоит из ' + str(self.part1) + ' и ' + str(self.part2)


class Lava:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Лава. Состоит из ' + str(self.part1) + ' и ' + str(self.part2)


element_1 = Water()
element_2 = Air()
element_3 = Fire()
element_4 = Earth()
result_1 = element_1 + element_2
result_2 = element_1 + element_3
result_3 = element_1 + element_4
result_4 = element_2 + element_3
result_5 = element_2 + element_4
result_6 = element_3 + element_4
print(result_1)
print(result_2)
print(result_3)
print(result_4)
print(result_5)
print(result_6)
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
