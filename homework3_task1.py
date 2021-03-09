# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9


MIN = 2
MAX = 9
result = {x: 0 for x in range(MIN, MAX)}

for num in range(2, 99):
    for devisor in range(MIN, MAX):
        if num % devisor == 0:
            result[devisor] += 1

for key, val in result.items():
    print(f'Для числа {key} -> кратных ему чисел {val}')
