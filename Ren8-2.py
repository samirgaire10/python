
num = int(input("整数入力＞＞"))

if num < 0 or num > 100:
	print("点数は0以上100の範囲ば入力してください")

elif num >= 0 and num < 60:
	print("評価はDです")


elif num >= 60 and num < 70:
	print("評価はCです")


elif num >= 70 and num < 80:
	print("評価はBです")


elif num >= 80 and num < 90:
	print("評価はAです")


elif num > 90 and num <= 100:
	print("評価はSです")