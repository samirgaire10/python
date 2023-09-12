
one  = int(input("1つ目の値入力>>"))
two  = int(input("２つ目の値入力>>"))
if one > two :
    ans= one-two
    print("大きい値から小さい値を引いた答えは{}です".format(ans))
else:
    ans= two - one
    print("大きい値から小さい値を引いた答えは{}です".format(ans))

