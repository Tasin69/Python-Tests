data = open('F:\ML\Side Quests\Python\Assignments-Chuck Py DS\mbox-short.txt')
hour_dict = dict()

for line in data:
    if line.endswith('2008\n'):
        temp_list = line.split()
        time = temp_list[-2].split(':')
        hour_dict[time[0]] = hour_dict.get(time[0], 0) + 1

sorted_hour = sorted(hour_dict.items())
for k,v in sorted_hour:
    print(k, int(v/2))