def get_score(game_result):
    possible_values = {'1': 1, '2': 2, '3': 3, '4': 4,
                       '5': 5, '6': 7, '7': 7, '8': 8, '9': 9,
                       '-': 0, '/': 1, 'x': 20, 'X': 20, 'х': 20, 'Х': 20}
    count_x, without_strike = check_strike(game_result)
    values_list = check_data(count_x, game_result, possible_values, without_strike)
    total = counting_values(count_x, possible_values, values_list)
    return total


def counting_values(count_x, possible_values, values_list):
    total = 0
    for value in values_list:
        if '/' in value:
            total += 15
            continue
        for char in value:
            total += possible_values[char]
    total += count_x * 20
    return total


def check_data(count_x, game_result, possible_values, without_strike):
    date = game_result
    max_len = 40 - count_x * 2
    for char in date:
        if char in possible_values:
            continue
        else:
            raise ValueError(f'{char} не допустимое значение')
    if len(without_strike) > max_len:
        raise Exception('Ошибка при вводе. Значений больше допустимого')
    values_list = [without_strike[i:i + 2] for i in
                   range(0, len(without_strike), 2)]  # разобьем строку на пары значений
    for stroka in values_list:
        if stroka.startswith('/'):
            raise Exception(f"пара значений {stroka} начинается с {'/'}")
    return values_list


def check_strike(game_result):
    date = game_result
    strike_list = ['x', 'X', 'х', 'Х']
    count_x = 0
    for x in strike_list:
        if x in date:
            count_x += date.count(x)
            date = date.replace(x, '')
    return count_x, date


if __name__ == '__main__':
    print(get_score('x47117'
                    '154--/554/'))
