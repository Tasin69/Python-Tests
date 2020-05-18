romeo = open('F:\ML\Side Quests\Python\Assignments-Chuck Py DS\Romeo.txt')
rom_dic = dict()

for line in romeo:
    words = line.split()
    for key in words:
        rom_dic[key] = rom_dic.get(key, 0) + 1

print(rom_dic)
bigcount = None
bigword = None
for k,v in rom_dic.items():
    if bigcount is None or v > bigcount:
        bigcount = v
        bigword = k
print("\nBiggest word occurance - ", bigword, ":" , bigcount)