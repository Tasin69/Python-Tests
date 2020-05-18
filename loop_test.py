j = 0
x = [1, 2, 3, 4]

for i in x:
    if i in x:
        continue
    else:
        print("noice")
else:
    j += 1

print(j)