
def kasan(w_ope1,w_ope2):
    total = w_ope1 + w_ope2
    print("{}+{}={}".format(w_ope1,w_ope2,total))



print("加算プログラムVer.2")
w_ope1 = int(input("1つめのオペランド>>"))
w_ope2 = int(input("2つめのオペランド>>"))

kasan(w_ope1,w_ope2)
