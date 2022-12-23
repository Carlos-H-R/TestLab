import random

m = []

for i in range(100):
    m.append(random.randint(1,6))

for i in range(1,7):
    print("A face %i apareceu %i vezes."%(i, m.count(i)))
