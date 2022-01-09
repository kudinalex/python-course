import random
s = []
q = []
count = 0
while count != 7:
    x = random.randint(1,49)
    if x not in s:
        q.append(x)
        s.append(x)
        count += 1
print(*sorted(q))  
