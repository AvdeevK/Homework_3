# 4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(f'Исходный массив {array=}')

temp_el = array[0]
temp_count = 0

for index in range(len(array)):
    counter = 0
    for i in range(index, len(array)):
        if array[i] == array[index]:
            counter += 1

    if counter > temp_count:
        temp_count = counter
        temp_el = array[index]

print(f'Наимболее часто встречающееся число: {temp_el}, оно встречается {temp_count} раз')

