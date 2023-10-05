import math
array = [[-1, -2, 3, 4], [5, -6, 7, 8], [9, -10, 11, 12]]
sum_even_positive = 0
for sublist in array:
    for element in sublist:
        if element > 0 and element % 2 == 0:
            sum_even_positive += element
if sum_even_positive > 0:
    print("Сумма четных положительных элементов:", sum_even_positive)
else:
    print("В исходном массиве нет четных положительных элементов.")