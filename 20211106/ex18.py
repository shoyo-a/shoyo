import random

circle = 0
time = int(input('実行回数> '))

for cnt in range(time):
    x = random.random()
    y = random.random()

    if (x ** 2) + (y ** 2) <= 1:
        circle += 1

print('PI = ' + str(circle * 4 / time))