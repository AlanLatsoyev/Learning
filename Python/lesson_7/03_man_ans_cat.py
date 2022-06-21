# -*- coding: utf-8 -*-

from random import randint, choice

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.
from termcolor import cprint


class Home:
    def __init__(self):
        self.cat_food = 0
        self.mud = 0
        self.man_food = 0

    def __str__(self):
        return 'Количество кошачей еды-{}, Уровень загрезнения в доме-{}'.format(self.cat_food, self.mud)


class Cat:
    name = ['Мурзик', 'Рыжик', 'Снежок', 'Соня', 'Барсик']

    def __init__(self):
        self.name = choice(Cat.name)
        self.fullness = 0
        self.home = None

    def eat(self):
        self.fullness += 20
        self.home.cat_food -= 10
        cprint('Кот {} поел! Сытость увеличелась на-{}. Количество еды уменьшилось на-{}'.format(self.name, 20, 10),
               color='green')

    def sleep(self):
        self.fullness -= 10
        cprint('Кот высполся но немного проголодался:)')

    def tear_wallpaper(self):
        self.fullness -= 10
        self.home.mud += 5

    def choice_of_actions(self):
        if self.fullness < 10:
            if self.home.cat_food >= 10:
                self.eat()
            else:
                cprint('!!!!====Котик {} помер с голоду ;((====!!!!'.format(self.name), color='red')
            return
        cat_choice = randint(0, 1)
        if cat_choice == 0:
            self.sleep()
        else:
            self.tear_wallpaper()


class Man:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.fullness = 0
        self.home = Home()

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def buy_food_for_yourself(self):
        if self.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.money -= 50
            self.home.man_food += 50
        else:
            cprint('{} деньги закончились. Пора на работу !'.format(self.name), color='red')

    def buy_cat_food(self):
        if self.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.money -= 50
            self.home.cat_food += 50
        else:
            cprint('{} деньги закончились. Пора на работу !'.format(self.name), color='red')

    def clean_up_the_house(self):
        self.home.mud -= 100
        self.fullness -= 20
        self.money -= 10

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.money += 150
        self.fullness -= 10

    def pick_up_cat(self):
        Cat.home = Home
        self.money += 50

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.home.man_food < 10:
            self.buy_food_for_yourself()
        elif self.home.cat_food < 10:
            self.buy_cat_food()
        elif self.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()

    def eat(self):
        if self.home.man_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.home.man_food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
