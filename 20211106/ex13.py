num = int(input('数> '))

result = 1

for cnt in range(num):
    result *= (cnt + 1)

print(str(num) + '! = ' + str(result))