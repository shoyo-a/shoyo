year = int(input('西暦で年を入力してください'))
flg = 0
print(str(year) + '年は', end = '')
if year % 4 == 0:
    pass
else:
    if year % 100 == 0:
        pass
    else:
        flg = 1

if flg == 0:
    print('うるう年です。')
else:
    print('うるう年ではありません')