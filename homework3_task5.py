# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

SIZE = 10
MIN_ITEM = -50
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив {array=}')

for i in range(len(array)):
    if array[i] < 0:
        min_el = array[i]
        break

if min_el is not None:
    for i in enumerate(array):
        if i[1] < 0 and i[1] > min_el:
            min_el = i[1]

    print(f'Самое большое число среди отрицательных {min_el}')

else:
    print('Массив не содержит отрицательных чисел')


