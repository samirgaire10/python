import math
print("べき乗を行います")
num1 = int(input("元の値>>"))
num2 = int(input("何乗しますか＞＞"))
beki = math.pow(num1,num2)
print("{}の{}乗は{}です".format(num1,num2,beki))

num = float(input("小数入カ>>"))
sute = math.floor(num)
print("小数点以下切り捨て後:{}".format(sute))

age=  math.ceil(num)
print("小数点以下切り上げ後:{}".format(age))








