#Быстрая сортировка
import random
import time

start = time.time()
arr = [random.randint(1, 100) for _ in range(1000000)]

def bistro_sort(arr):
    n = len(arr)
    if len(arr) <= 1:
        return arr
    x = arr[0]
    left = []
    right = []
    ravno = []

    for i in arr:
        if i < x:
            left.append(i)
        elif i == x:
            ravno.append(i)
        else:
            right.append(i)
    left = bistro_sort(left)
    right = bistro_sort(right)
    return left + ravno + right
sort_arr = bistro_sort(arr)
finish = time.time()

time = finish - start
print("Отсортированный массив:", sort_arr)
print("Время:", time, "секунд")