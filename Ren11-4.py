def heikin(w_cd68):
    avg = sum(w_cd68) / len(w_cd68)
    # print("4クラス平均:{}点".format(avg))
    return avg
print("クラフス平均表示プログラムVer.2")

cd68 = list()
for num in range(4):
    ten = int(input("{}組の点数>>".format(num+1)))
    cd68.append(ten)
kekka = heikin(cd68)
print("4クラス平均:{}点".format(kekka))
