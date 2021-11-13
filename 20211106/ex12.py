num1 = int(input('数1> '))
num2 = int(input('数2> '))
num3 = int(input('数3> '))

nums = [num1, num2, num3]

max_num = max(nums)
min_num = min(nums)
middle = 0

if num1 == num2:
    middle = num1
elif num2 == num3:
    middle = num2
elif num3 == num1:
    middle = num3

for num in nums:
    if not (num == max_num or num == min_num):
        middle = num

print(str(min_num) + ' ' + str(middle) + ' ' + str(max_num))
