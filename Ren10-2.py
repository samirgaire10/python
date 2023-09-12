
num =  int(input("いくつの段を練習しますか?1-9を入力>>"))

for i in range(1,10):
    total = num * i
    print("{}✕{}={}".format(num, i, total))