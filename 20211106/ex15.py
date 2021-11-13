num = int(input('数> '))
for cnt in range(num):
    print(str(cnt + 1) + ':', end = '')
    for  cnt1 in range(cnt + 1):
        print('■', end = '')
    print()