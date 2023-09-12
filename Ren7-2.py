
gakkaCD = "CDISNT"
srch = input("探したい学科コード入力してください")

if srch in gakkaCD:
    print("文字例に{}が見つけました".format(srch))
else:
    print("文字列内に{}は見つかりません。".format(srch))
