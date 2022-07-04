# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# который читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234
def log_parser(file_name):
    prev_date = None
    events_count = 0
    with open(file_name, 'r', encoding='cp1251') as file:
        for line in file:
            date, time, event = line.split(' ')
            date_time = date +' '+ time
            next_date = date_time[1:17]
            if not prev_date:
                prev_date = next_date
            if prev_date == next_date:
                if event.startswith('N'):
                    events_count += 1
                    continue
                continue
            else:
                yield prev_date, events_count
                prev_date = next_date
                events_count = 0
                if event.startswith('N'):
                    events_count += 1


grouped_events = log_parser('events.txt')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')






