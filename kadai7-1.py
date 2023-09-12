
one  = int(input("1つ目の値入力>>"))
two  = int(input("２つ目の値入力>>"))
if one > two :
    ans= one-two
    print("大きい方から小さい方を引くと{}-{}で答えは{}".format(one,two,ans))
else:
    ans= two - one
    print("大きい方から小さい方を引くと{}-{}で答えは{}".format(one,two,ans))
