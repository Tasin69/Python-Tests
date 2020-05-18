romeo = open('F:\ML\Side Quests\Python\Assignments-Chuck\Romeo.txt')
rom_dic = dict()

for line in romeo:
    words = line.split()
    for key in words:
        rom_dic[key] = rom_dic.get(key, 0) + 1

top_ten = sorted([(v,k) for k,v in rom_dic.items()], reverse=True)

for v,k in top_ten[:10]:
    print(k, ':' ,v)