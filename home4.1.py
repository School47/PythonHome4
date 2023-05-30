set1 = set([2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2])
set2 = set([3, 6, 9, 12, 15, 18])

common = sorted(list(set1 & set2))

if common:
    print(" ".join([str(num) for num in common]))
else:
    print("Повторяющихся чисел нет")