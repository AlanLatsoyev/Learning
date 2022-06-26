# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import zipfile
from pprint import pprint


class Log_parser:
    def __init__(self, file_name):
        self.file_name = file_name
        self.total = 0
        self.stat = {}
        self.parsing_mode = 17

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def parsing(self, mode):
        if mode == 0:
            self.parsing_mode = 17
        elif mode == 1:
            self.parsing_mode = 14
        elif mode == 2:
            self.parsing_mode = 11
        elif mode == 3:
            self.parsing_mode = 8
        else:
            return print('Выбран не правильный режим')

        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                if line[1:self.parsing_mode] not in self.stat:
                    self.stat[line[1:self.parsing_mode]] = 0
                if line[29] == 'N':
                    self.stat[line[1:self.parsing_mode]] += 1

    def write_in_fail(self, out_file_name=None):

        if out_file_name is not None:
            file = open(out_file_name, 'w', encoding='utf8')
        else:
            file = None

        for i in self.stat:
            file.write(f"[{i}] {self.stat[i]}\n")
        if file:
            file.close()

        # pprint(self.stat)

    # print(line[1:17])
    # for char in line:
    #     print(f"{char}==={line.index(char)}")
    # break


fail_name = Log_parser(file_name='events.txt')
fail_name.parsing(mode=1)
fail_name.write_in_fail(out_file_name='out_file.txt')
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
