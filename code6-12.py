"""

profile = input("学科記号、名前の順で、カンマ区切りで入力>>")
[gakka, name ] = profile.split(',')
gakka = gakka.upper().strip()
print("{}科の{}さん、占いは凶です".format(gakka,name))