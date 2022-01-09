def generate_index():
    import random
    s = ''
    for i in range(2):
        x = random.randint(65,90)
        s += chr(x)
    y = random.randint(0,99)
    s += str(y)
    s += '_'
    y = random.randint(0,99)
    s += str(y)
    for i in range(2):
        x = random.randint(65,90)
        s += chr(x)
    return s
