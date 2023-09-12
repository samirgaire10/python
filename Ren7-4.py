
num   = int(input("1つ目の値入力>>"))
wk = num%2
if  wk == 0:
    ans = "偶数"
else:
    ans = "奇数"
print("値は{}です".format(ans))
