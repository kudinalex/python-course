import random

n = int(input())    # количество попыток
for i in range(n):
    x = random.randint(0,1)
    if x == 1:
        print('Орел')
    else:
        print('Решка')
