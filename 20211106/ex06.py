def calculate_goldspecies(amount):
    num = 0

    num = int(amount / 10000)
    print("一万円札= " + str(num) + " 枚")
    if num > 0:
        amount = amount - (num * 10000)
    
    num = int(amount / 5000)
    print("五千円札= " + str(num) + " 枚")
    if num > 0:
        amount = amount - (num * 5000)
    
    num = int(amount / 1000)
    print("千円札  = " + str(num) + " 枚")
    if num > 0:
        amount = amount - (num * 1000)
    
    num = int(amount / 500)
    print("五百円玉= " + str(num) + " 枚")
    if num > 0:
        amount = amount - (num * 500)
    
    num = int(amount / 100)
    print("百円玉  = " + str(num) + " 枚")
    if num > 0:
        amount = amount - (num * 100)
    
    num = int(amount / 50)
    print("五十円玉= " + str(num) + " 枚")
    if num > 0:
        amount = amount - (num * 50)
    
    num = int(amount / 10)
    print("十円玉  = " + str(num) + " 枚")
    if num > 0:
        amount = amount - (num * 10)
    
    num = int(amount / 5)
    print("五円玉  = " + str(num) + " 枚")
    if num > 0:
        amount = amount - (num * 5)
    
    num = amount
    print("一円玉  = " + str(num) + " 枚")

sum = int(input('金額(円)> '))
print("金額: " + str(sum) + " 円")
calculate_goldspecies(sum)
