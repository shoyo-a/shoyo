decimal = int(input('10進数> '))
binary = format(decimal, 'b')
if len(binary) < 8:
    cnt = 8 - len(binary)
    for num in range(cnt):
        binary = "0" + binary

print(str(decimal) + " = " + binary)