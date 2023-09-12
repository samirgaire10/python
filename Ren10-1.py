data = 0 
total = 0
is_rpt = True
while is_rpt :
    data = int(input("加算する数値を入力>>"))
    total = total + data
    key = input("計算 を 継続 し ます か ? 継続 :y プ 終了 :n -->>")
    if key == 'n':
        is_rpt = False

print("合計は{}です".format(total))
    





