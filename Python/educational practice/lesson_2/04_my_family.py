#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []
dad = ['Taymuraz', 178]
mam = ['Ekaterina', 176]
brother = ['Roman', 180]
# список списков приблизителного роста членов вашей семьи
my_family_height = [dad, mam, brother]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см


print('Рост отца -', int(my_family_height[0][1]), 'см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
all_height = int(my_family_height[0][1]) + int(my_family_height[1][1]) + int(my_family_height[2][1])
print('Общий рост моей семьи -', all_height, 'см')
