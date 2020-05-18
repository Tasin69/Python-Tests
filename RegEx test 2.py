import re

data = open('F:\ML\Side Quests\Python\Assignments-Chuck Py DS\mbox-short.txt')
x = data.read()
hour_dict = dict()

y = re.findall('^From.+\s(\d+):' ,x)
print(y)