import random
string = "qwertyuipasdfghjkzxcvbnmQWERTYUPASDFGHJKLZXCVBNM23456789"
def generate_passwords(count, length):
    r = []
    for i in range(length):
        x = []
        s = ''
        for j in range(count):
            y = random.sample(string,1)
            x.extend(y)
        for q in range(len(x)):
            s += x[q]
        r.append(s)
    return r
n, m = int(input()), int(input())
l = generate_passwords(m,n)
for k in range(len(l)):
    print(l[k], end='\n')
