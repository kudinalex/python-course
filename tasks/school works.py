x = 0
while str(bin(x))[2:] != '11010010':
    x += 1
print(str(bin(x))[2:])