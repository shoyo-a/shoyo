import random
comp = random.randint(0, 2)
janken = {0 : 'グー', 1 : 'チョキ', 2 : 'パー'}
print('ジャンケンポン！')
you = int(input('あなたは？(0:グー, 1:チョキ, 2:パー)> '))
print('わたしは' + janken[comp] + '。あなたは' + janken[you] + '。', end = '')
if you == comp:
    print('あいこです。')
else:
    print('あなたの', end = '')
    if you == 0:
        if comp == 1:
            print('勝ちです。')
        else:
            print('負けです。')
    elif you == 1:
        if comp == 0:
            print('負けです。')
        else:
            print('勝ちです。')
    else:
        if comp == 0:
            print('勝ちです。')
        else:
            print('負けです。')

