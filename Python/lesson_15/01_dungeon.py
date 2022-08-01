# -*- coding: utf-8 -*-

# С помощью JSON файла rpg.json задана "карта" подземелья.
# Подземелье было выкопано монстрами и они всё ещё скрываются где-то в его глубинах,
# планируя набеги на близлежащие поселения.
# Само подземелье состоит из двух главных разветвлений и нескольких развилок,
# и лишь один из путей приведёт вас к главному Боссу
# и позволит предотвратить набеги и спасти мирных жителей.

# Напишите игру, в которой пользователь, с помощью консоли,
# сможет:
# 1) исследовать это подземелье:
#   -- передвижение должно осуществляться присваиванием переменной и только в одну сторону
#   -- перемещаясь из одной локации в другую, пользователь теряет время, указанное в конце названия каждой локации
# Так, перейдя в локацию Location_1_tm500 - вам необходимо будет списать со счёта 500 секунд.
# Тег, в названии локации, указывающий на время - 'tm'.
#
# 2) сражаться с монстрами:
#   -- сражение имитируется списанием со счета персонажа N-количества времени и получением N-количества опыта
#   -- опыт и время указаны в названиях монстров (после exp указано значение опыта и после tm указано время)
# Так, если в локации вы обнаружили монстра Mob_exp10_tm20 (или Boss_exp10_tm20)
# необходимо списать со счета 20 секунд и добавить 10 очков опыта.
# Теги указывающие на опыт и время - 'exp' и 'tm'.
# После того, как игра будет готова, сыграйте в неё и наберите 280 очков при положительном остатке времени.

# По мере продвижения вам так же необходимо вести журнал,
# в котором должна содержаться следующая информация:
# -- текущее положение
# -- текущее количество опыта
# -- текущая дата (отсчёт вести с первой локации с помощью datetime)
# После прохождения лабиринта, набора 280 очков опыта и проверки на остаток времени (remaining_time > 0),
# журнал необходимо записать в csv файл (назвать dungeon.csv, названия столбцов взять из field_names).

# Пример лога игры:
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 1234567890.0987654321 секунд
# Прошло уже 0:00:00
# Внутри вы видите:
# -- Монстра Mob_exp10_tm0
# -- Вход в локацию: Location_1_tm10400000
# -- Вход в локацию: Location_2_tm333000000
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Выход
import csv
import json
import re
from datetime import datetime
from decimal import Decimal


# если изначально не писать число в виде строки - теряется точность!


def what_inside(date):
    content = []
    count = 1
    print(f"{'Внутри вы видите:':-^50}")
    for value in date:
        if type(value) == str:
            content.append(value)
            print(f"{'':9}{count} - Монстра {value}")
            count += 1
        elif type(value) == dict:
            for key in value.keys():
                content.append(key)
                print(f"{'':9}{count} - Вход в локацию: {key}")
                count += 1
        elif type(value) == list:
            for obj in value:
                content.append(obj)
                print(f"{'':9}{count} -- {obj}")
                count += 1

    return content, count


def make_choice(count):
    player_choice = input(f"{'Сделайте выбор согласно нумерации:':-^50}\n"
                          f"{'':9}{'Атаковать монстра'}\n"
                          f"{'':9}{'Перейти на другую локацию'}\n"
                          f"{'':9}{str(count) + ' - Выход из игры'}\n")
    if 0 < int(player_choice) <= count:
        print(f"Вы выбрали {player_choice}")
        return int(player_choice)
    else:
        print(f"Вы допустили ошибку при вводе! ")
    return player_choice


def action(date, content, player_choice):
    if int(player_choice) == len(content) + 1:
        return False
    key = content[int(player_choice) - 1]
    for value in date:
        if key in value:
            if type(value) == list:
                value.remove(key)
            elif type(value) == str:
                date.remove(key)
            elif type(value) == dict:
                date = value[key]

    return date


def get_values(player_chose, location, player_exp, remaining_time):
    local_re = r'Location_(\w*\d+)_tm(\d+.*\d*)'
    mob_re = r'Mob_exp(\d+.*\d*)_tm(\d+.*\d*)'
    boss_re = r'Boss\d*_exp(\d+.*\d*)_tm(\d+.*\d*)'
    re_list = [local_re, mob_re, boss_re]
    for reg in re_list:
        matched = re.search(reg, player_chose)
        if matched:
            if reg == re_list[0]:
                location = player_chose
                remaining_time -= Decimal(matched[2])
            else:
                player_exp += int(matched[1])
                remaining_time -= Decimal(matched[2])
    return location, player_exp, remaining_time


def write_in_csv(list_values, field_names):
    with open('dungeon.csv', 'w', newline='') as out_csv:
        writer = csv.DictWriter(out_csv, delimiter=',', fieldnames=field_names)
        writer.writeheader()
        writer.writerows(list_values)


def run():
    with open('rpg.json', 'r') as json_file:
        date = json.load(json_file)
    location = list(date.keys())[0]
    date = date[location]
    player_exp = 0
    given_time = '1234567890.0987654321'
    remaining_time = Decimal(given_time)
    start_time = datetime.now()
    list_values = []
    field_names = ['current_location', 'current_experience', 'current_date']

    while date:
        time_now = datetime.now() - start_time
        print(f'Вы находитесь в {location}\n'
              f'У вас {player_exp} опыта и осталось {remaining_time} секунд\n'
              f'Прошло уже {time_now}')
        list_values.append({field_names[0]: location,
                            field_names[1]: player_exp,
                            field_names[2]: time_now})
        content, count = what_inside(date)
        player_choice = make_choice(count)
        date = action(date=date, content=content, player_choice=player_choice)
        if date:
            player_choice = content[player_choice - 1]
        else:
            break
        location, player_exp, remaining_time = get_values(player_chose=player_choice,
                                                          location=location,
                                                          player_exp=player_exp,
                                                          remaining_time=remaining_time)
    write_in_csv(list_values=list_values, field_names=field_names)


if __name__ == '__main__':
    run()

# Учитывая время и опыт, не забывайте о точности вычислений!
