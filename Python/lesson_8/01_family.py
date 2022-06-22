# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько cъедено еды, сколько куплено шуб.


class Human:

    def __init__(self, home):
        self.fullness = 30
        self.happiness = 100
        self.home = home

    def eat(self):
        if self.home.man_food >= 30:
            self.fullness += 30
            self.home.man_food -= 30
            self.home.total_ate_food += 30
            return True
        elif self.home.man_food < 30:
            cprint('Нет еды', color='red')

    def act(self):
        if self.fullness < 30:
            self.eat()
        self.home.mud += 5
        if self.home.mud >= 90:
            self.happiness -= 10

    def __str__(self):
        return ' Сытость-{} Уровень счастья-{}'.format(self.fullness, self.happiness)


class House:
    total_money = 100
    total_buy_fur_coat = 0
    total_ate_food = 0

    def __init__(self):
        self.money = 100
        self.man_food = 50
        self.mud = 0

    def __str__(self):
        return 'Еды в доме = {} денег {} грязь {}'.format(self.man_food, self.money, self.mud)

class Husband(Human):
    def __init__(self, name, home):
        super().__init__(home=home)
        self.name = name


    def __str__(self):
        res = super().__str__()
        return 'У {}'.format(self.name) + res

    def eat(self):
        if super().eat():
            cprint('{} поел'.format(self.name), color='yellow')
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.home.money += 150
        home.total_money += 150
        self.fullness -= 10
        self.happiness -= 10

    def gaming(self):
        cprint('{} играл весь день'.format(self.name), color='green')
        self.fullness -= 10
        self.happiness += 20

    def act(self):
        dice = randint(1, 6)
        super().act()
        if self.fullness <= 0:
            cprint('{} умер с голоду...'.format(self.name), color='red')
        elif self.happiness <= 0:
            cprint('{} умер от депрессии...'.format(self.name), color='red')
        if self.home.money <= 60:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.gaming()


class Wife(Human):

    def __init__(self, name, home):
        super().__init__(home=home)
        self.name = name

    def __str__(self):
        res = super().__str__()
        return 'У {}'.format(self.name) + res

    def eat(self):
        if super().eat():
            cprint('{} поел'.format(self.name), color='yellow')
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def shopping(self):
        if self.home.money >= 60:
            cprint('{} сходила в магазин за едой '.format(self.name), color='magenta')
            self.home.money -= 60
            self.home.man_food += 60
            self.home.total_ate_food += 60
        else:
            cprint(' Деньги закончились. Пора на работу !', color='red')

    def buy_fur_coat(self):
        self.home.money -= 350
        self.happiness += 60
        self.home.total_buy_fur_coat += 1

    def clean_house(self):
        self.home.mud -= 100
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрела MTV целый день'.format(self.name), color='green')
        self.fullness -= 10
        #self.happiness += 10

    def act(self):
        dice = randint(1, 6)
        super().act()
        if self.fullness <= 0:
            cprint('{} умер с голоду...'.format(self.name), color='red')
        elif self.happiness <= 0:
            cprint('{} умер от депрессии...'.format(self.name), color='red')
        if self.home.man_food <= 60:
            self.shopping()
        elif self.home.mud >= 100:
            self.clean_house()
        elif self.happiness < 60:
            self.buy_fur_coat()
        elif dice == 1:
            self.shopping()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


home = House()
serge = Husband(name='Сережа', home=home)
masha = Wife(name='Маша', home=home)

for day in range(1, 365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    print(serge)
    print(masha)
    print(home)
    cprint('Всего еды было куплено {}'.format(home.total_ate_food), color='yellow')
    cprint('Всего шуб было куплено {}'.format(home.total_buy_fur_coat), color='yellow')
    cprint('Всего денег заработано {}'.format(home.total_money), color='yellow')

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


# class Cat:
#
#     def __init__(self):
#         pass
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass
#

######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

# class Child:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#
# # TODO после реализации второй части - отдать на проверку учителем две ветки
#

######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')
#

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

