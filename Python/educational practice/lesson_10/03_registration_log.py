# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def exam(line):
    name, email, age = line.split(' ')
    if name and email and age is None:
        raise ValueError('НЕ присутсвуют все три поля')
    if not (name.isalpha()):
        raise NotNameError('имя введено не верно или содержит цифру')
    if not ('.' and '@' in email):
        raise NotEmailError('email введен не верно')
    if not (10 < int(age) < 99):
        raise ValueError('возраст не попадает в промежуток от 10 до 99')
    with open('registrations_good.log', 'a', encoding='utf8') as fr:
        fr.write(line)

with open('registrations.txt', 'r', encoding='utf8') as ff:
    for line in ff:

        try:
            exam(line)
        except (ValueError, NotNameError, NotEmailError) as exc:
            with open('registrations_bad.log', 'a', encoding='utf8') as fr:
                fr.write(f'В строке {line} ошибка вида {exc} ')
