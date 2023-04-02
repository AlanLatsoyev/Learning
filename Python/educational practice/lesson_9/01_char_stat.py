# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import zipfile
from pprint import pprint

from termcolor import cprint


class Char_stat:
    def __init__(self, file_name):
        self.file_name = file_name
        self.total = 0
        self.stat = {}
        self.stat_sorted = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()

        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.stat:
                            self.stat[char] += 1
                            self.total += 1
                        else:
                            self.stat[char] = 1
                            self.total += 1
        # print(self.stat)
        # print(self.total)
        # print(file.name)
        # print(file.closed)

    def stat_sort(self, sort=1, reverse=False):
        self.stat_sorted = sorted(self.stat.items(), key=lambda x: x[sort], reverse=reverse)

    def print_stat_sort(self):
        cprint(f"|{'-' * 15}+{'-' * 15}|", color='red')
        cprint(f"|{'буква':^15}|{'частота':^15}|", color='red')
        cprint(f"|{'-' * 15}+{'-' * 15}|", color='red')
        for i in self.stat_sorted:
            cprint(f"|{i[0]:^15}|{i[1]:^15}|", color='yellow')

        cprint(f"|{'-' * 15}+{'-' * 15}|", color='red')
        cprint(f"|{'Итого':^15}|{self.total:^15}|", color='red')
        cprint(f"|{'-' * 15}+{'-' * 15}|", color='red')







char_stat = Char_stat(file_name='python_snippets\\voyna-i-mir.txt.zip')
char_stat.collect()
char_stat.stat_sort(sort=0, reverse=False)
char_stat.print_stat_sort()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
