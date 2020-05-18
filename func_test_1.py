def str_output(n, in_str):
    out  = n * in_str
    return out

x = int(input("Length of string to be multiplied: "))
y = input("The string: ")
z = str_output(x, y)
print("\nOutput: ",z)