
def in_ninzu(it):
    print("{}の各人数を入力します".format(it))
    zaiseki = int(input("在籍数>>"))
    goukaku = int(input("基本情報試験合格者数>>"))
    ninzu = [zaiseki , goukaku]
    return ninzu

def wariai_keisan(ninzu):
    ritu = ninzu[1] / ninzu[0] * 100
    return ritu

def out_ritu(it,ritu):
    print("{}のFE取得率は{}%".format(it,ritu))
    



cd_ninzu = in_ninzu('情報処理科')
is_ninzu = in_ninzu("ITスペシャリスト科")
cd_ritu = wariai_keisan(cd_ninzu)
is_ritu = wariai_keisan(is_ninzu)
out_ritu("情報処理科",cd_ritu)
out_ritu("ITスペシャリスト科",is_ritu)

