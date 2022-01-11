import random
s = []
q = []
y = ''
for i in range(1,76):
    s.append(i)
q = random.sample(s, 25)
q[12] = 0
for j in range(25):
    if (j + 1) % 5 == 0:
        print(q[j], end='\n')
    else:
        print(q[j], end = ' ')
