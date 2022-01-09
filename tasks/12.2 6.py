def generate_ip():
    import random
    s = []
    for i in range(4):
        x = random.randint(0,255)
        s.append(str(x))
    return '.'.join(s)
