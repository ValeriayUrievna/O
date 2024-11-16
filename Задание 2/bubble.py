import random
array = [random.randint(1, 100) for _ in range(1000000)]

def bubble_sort_descending(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

sorted_array = bubble_sort_descending(array)
print(sorted_array)