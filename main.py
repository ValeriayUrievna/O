def f(b,c):
    a = int(input("Введите число а  "))
    if a>0:
        return max(a,b,c)
    else:
        return -1
print("Вывод: ", f(8,2))