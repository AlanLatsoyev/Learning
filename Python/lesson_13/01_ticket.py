# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
import os

from PIL import Image, ImageDraw, ImageFont, ImageColor


def make_ticket(fio, from_, to_, date):
    font_path = os.path.join('python_snippets', "fonts", "ofont.ru_Myriad Pro Cond.ttf")
    template = os.path.join("images", "ticket_template.png")
    im = Image.open(template)
    print(im)
    coordinates = {fio: (45, 125), from_: (45, 195), to_: (45, 260), date: (280, 260)}
    for text, coordinate in coordinates.items():
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(font_path, size=20)
        x = coordinate[0]
        y = coordinate[1]
        message = f" {text}"
        draw.text((x, y), message, font=font, fill=ImageColor.colormap['black'])
    im.show()


if __name__ == '__main__':
    fio = 'Иванов И.И'
    from_ = 'Москва'
    to_ = 'Питер'
    date = '19.02'
    make_ticket(fio=fio, from_=from_, to_=to_, date=date)

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
