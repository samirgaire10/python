
atai1 = str(input("１つめの値＝"))
atai2 = str(input("2つめの値="))

print("１つめの値＝{},１つめの値＝{}".format(atai1,atai2))
flg = int(input("入力区分絶対値計算:1///文字連 結:2>>>>"))


if flg == 2:
	print("文字を連結すると{}{}です".format(atai1,atai2))

elif flg == 1:
	atai1 = int(atai1)
	atai2 = int(atai2)
	if atai1 > atai2:
		print("絶対値は{}です".format(atai1-atai2))
	if atai1 < atai2:
		print("絶対値は{}です".format(atai2-atai1))
