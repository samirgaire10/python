

keisan  = int(input("計算しますか?(する:1/しない:0)"))
if keisan == 1 :
	num1 = int(input("１つめのオペランド>>"))
	cal = input("演算子")
	num2 = int(input("2つめのオペランド>>"))

	if cal == '+' :
		ans =  num1 + num2 
		print("答えるは{}".format(ans))
	
	elif cal == '-' :
		ans =  num1 - num2 
		print("答えるは{}".format(ans))
	
	elif cal == '*' :
		ans =  num1 * num2 
		print("答えるは{}".format(ans))

	
	elif cal == '/' :
		ans =  num1 * num2 
		print("答えるは{}".format(ans))
	
	else:
		print("計算できません")

else:
	print("計算希望なしなので終了します")