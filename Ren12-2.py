"""
IT = 'ITスペシャリスト科'


def it_print():
    global IT
    IT ='情報処理科'

print("変更前のグローバル変数ITの内容{}".format(IT))
it_print()
print("変更後のグローバル変数ITの内容:{}".format(IT))



