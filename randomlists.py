import random
a = list(range(random.randint(1, 20)))
b = list(range(random.randint(1, 20)))
c = []
for i in a and b:
    if i in a and b:
        c.append(i)
print(c)
