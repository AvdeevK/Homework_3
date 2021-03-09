# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Изначально массив имел вид {array=}')

temp_min = array[0]
i_min = 0
temp_max = array[0]
i_max = 0

for i in range(len(array)):
    if array[i] < temp_min:
        temp_min = array[i]
        i_min = i

    if array[i] > temp_max:
        temp_max = array[i]
        i_max = i

array[i_min] = temp_max
array[i_max] = temp_min

print(f'Массив после перестановки {array=}')
