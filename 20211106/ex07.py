height = float(input('身長をm単位で入力してください> '))
weight = float(input('体重をkg単位で入力してください> '))

bmi = weight / height / height
print("BMI = " + str(bmi))
print('あなたは「', end='')
if bmi < 18.5:
    print('やせ', end='')
elif bmi >= 30:
    print('高度肥満', end='')
else:
    print('標準', end='')

print('」です。')