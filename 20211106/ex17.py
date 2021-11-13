import math

debt = int(input('借金> '))
ratio = float(input('年利率(％)> '))
repay = int(input('返済額> '))
month = 1
total = 0
term = 0

ratio = (ratio / 100 / 12) + float(1)
while debt > 0:
    debt = math.floor(debt * ratio)
    if debt > repay:
        debt -= repay
    else:
        repay = debt
        debt -= repay
    total += repay

    if month > 12:
        month -= 12
    
    print(str(month) + '月: 返済額 ' + str(int(repay)) + ' 円', end = '')
    if debt > 0:
        print(' 残り ' + str(int(debt)) + '円')
    else:
        print('これで完済。　返済額:  ' + str(int(total)) + ' 円')
    
    term += 1
    month += 1

if term > 12:
    print('支払期間: ', str(int(term / 12)), '年', str(term % 12), 'カ月')
else:
    print('支払期間: ' + str(term) + 'カ月')