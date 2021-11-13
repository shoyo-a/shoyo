cnt = 0
num = 1
sum = 0

while num >= 0:
    num = int(input('データ入力(負の数で終了)> '))
    if not num < 0:
        cnt += 1
        sum += num

print('データ数: ' + str(cnt) + ' 合計: ' + str(sum) + ' 平均: ' + str(sum / cnt))