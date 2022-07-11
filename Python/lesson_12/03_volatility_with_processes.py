# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
import multiprocessing
import os
import time
from itertools import islice


class Extractor(multiprocessing.Process):
    def __init__(self, path, collector, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = path
        self.max_price = 0
        self.min_price = 0
        self.price_list = []
        self.average_price = 0
        self.volatility = 0
        self.ticker = None
        self.f = {}
        self.collector = collector

    def run(self):
        with open(self.path, 'r') as file:
            for line in islice(file, 1, None):
                secid, tradetime, price, quantity = line.split(',')
                price = float(price) / float(quantity)
                self.price_list.append(price)
                if self.ticker is None:
                    self.ticker = secid
        self.max_price = max(self.price_list)
        self.min_price = min(self.price_list)
        self.average_price = (self.max_price + self.min_price) / 2
        self.volatility = round((((self.max_price - self.min_price) / self.average_price) * 100), 2)
        print(f'{self.ticker}-{self.volatility}', flush=True)
        self.collector.put({self.ticker: self.volatility})


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result

    return surrogate


def get_list_of_files(path):
    path = os.path.normpath(path)
    list_of_file = []
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            full_file_path = os.path.join(dirpath, file)
            list_of_file.append(full_file_path)
    return list_of_file


def get_max_min_zero(tickers, max_quantity, min_quantity):
    dict_tickers = tickers.copy()
    dict_max_volatility = {}
    dict_min_volatility = {}
    dict_zero_volatility = {}
    for ticker, volatility in dict_tickers.items():
        if volatility == 0:
            dict_zero_volatility[ticker] = volatility
    for key in dict_zero_volatility.keys():
        if key in dict_tickers:
            del dict_tickers[key]
    for quantity in range(0, max_quantity):
        max_volatility = max(dict_tickers.values())
        for ticker, volatility in dict_tickers.items():
            if volatility == max_volatility:
                dict_max_volatility[ticker] = volatility
        for key in dict_max_volatility.keys():
            if key in dict_tickers:
                del dict_tickers[key]
    for quantity in range(0, min_quantity):
        min_volatility = min(dict_tickers.values())
        for ticker, volatility in dict_tickers.items():
            if volatility == min_volatility:
                dict_min_volatility[ticker] = volatility
        for key in dict_min_volatility.keys():
            if key in dict_tickers:
                del dict_tickers[key]
    return dict_max_volatility, dict_min_volatility, dict_zero_volatility


@time_track
def main():
    path = 'trades'
    list_of_file = get_list_of_files(path)
    tickers = {}
    collector = multiprocessing.Queue()

    files = [Extractor(path=path, collector=collector) for path in list_of_file]
    for file in files:
        file.start()
    for file in files:
        file.join()

    while not collector.empty():
        data = collector.get()
        tickers.update(data)

    print(tickers)
    print(len(tickers))

    dict_max_volatility, dict_min_volatility, dict_zero_volatility = \
        get_max_min_zero(tickers, max_quantity=5, min_quantity=10)

    print(f"|{'Максимальная волатильность':-^31}|")
    for key, value in dict_max_volatility.items():
        print(f"|{key:>14} - {str(value) + ' %':<14}|")

    print(f"|{'Минимальная волатильность':-^31}|")
    for key, value in dict_min_volatility.items():
        print(f"|{key:>14} - {str(value) + ' %':<14}|")

    print(f"|{'Нулевая волатильность':-^31}|")
    for ticker in dict_zero_volatility.keys():
        print(f"{ticker + ', '}", end='')
    print()


if __name__ == '__main__':
    main()
