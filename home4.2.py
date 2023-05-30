berries = [1, 2, 3, 4, 5, 6, 7, 8]

max_sum = 0
max_kust = 0

for i in range(len(berries)):
    sum = berries[i] + berries[(i-1)%len(berries)] + berries[(i+1)%len(berries)] # cобираем ягоды с текущего, предыдущего и следующего куста
    if sum > max_sum:    # если сумма полученных ягод больше уже найденной максимальной суммы, то обновляем ее
        max_sum = sum
        max_kust = i+1   # сохраняем номер куста (на 1 больше индекса в списке)
        
print("Макс. кол-во ягод", max_sum, ", собрано для куста", max_kust)
