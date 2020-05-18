x = [5, -2, 4, 8, 6, 5]
error = []
er_cz = []

for i in x:
    largest = 0
    for j in x:
        if abs(i - j) > largest:
            largest = abs(i - j)
            er_cz_temp = j
    error.append(largest)
    er_cz.append(er_cz_temp)

