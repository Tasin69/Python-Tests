from collections import Counter

x = [2, 3, 1, 2, 2, 5, 6, 2, 5, 3, 5]
occ = Counter(x)
print(occ.most_common(1)[0][0])
print(occ.most_common(1)[0][1])

x = set(x)
x.remove(2)
x = list(x)
print(x)