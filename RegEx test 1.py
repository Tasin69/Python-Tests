import re

data = open('F:\ML\Side Quests\Python\Assignments-Chuck Py DS\mbox-short.txt')
hour_dict = dict()

for line in data: 
    y = re.findall('^From.+\s(\d+):' ,line)
    if len(y) == 0: continue
    hour_dict[y[0]] = hour_dict.get(y[0], 0) + 1
print(hour_dict)

sorted_hour = sorted([(v,k) for k,v in hour_dict.items()], reverse=True)
for v,k in sorted_hour:
    print(k,':', v)