import random
s = ''
length = int(input())    # длина пароля
for i in range(length):
    x = random.randint(0,1)
    if x == 0:
        y = random.randint(65,90)
        s += chr(y)
    else:
        y = random.randint(97,122)
        s += chr(y)
print(s)
