year = int(input('年> '))
month = int(input('月> '))
day = int(input('日> '))
weekday = (year + (year // 4) - (year // 100) + (year // 400) + ((13*month+8) // 5) + day) % 7

if weekday == 0:
    days = '日'
elif weekday == 1:
    days = '月'
elif weekday == 2:
    days = '火'
elif weekday == 3:
    days = '水'
elif weekday == 4:
    days = '木'
elif weekday == 5:
    days = '金'
else:
    days = '土'

print(str(year) + '年' + str(month) + '月' + str(day) + '日は' + days + '曜日です。')