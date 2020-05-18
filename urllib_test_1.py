import urllib as ub

url_handle = ub.request.urlopen('http://data.pr4e.org/romeo.txt')

print("The txt data:")
for line in url_handle:
    print(line.decode())

url_handle = ub.request.urlopen('http://data.pr4e.org/romeo.txt').read()
print('In Byte:\n',url_handle)

url_data = ub.request.urlopen('http://data.pr4e.org/romeo.txt').read().decode()
print('\nDecoded (in string):\n',url_data)