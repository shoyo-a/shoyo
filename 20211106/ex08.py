day = int(input('数(0-6)> '))
if day < 0 or 6 < day:
    print('0から6までの数を入力してください')
else:
    if day == 0:
        print('日', end='')
    elif day == 1:
        print('月', end='')
    elif day == 2:
        print('火', end='')
    elif day == 3:
        print('水', end='')
    elif day == 4:
        print('木', end='')
    elif day == 5:
        print('金', end='')
    else:
        print('土', end='')
    print('曜日')