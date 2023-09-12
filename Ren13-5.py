
class lunchset:
    drink = "ココア"
    food = 'キッシュ'
    tanka = 1000
    kei  = 0 
    def naiyou(self):
        print("ランチセットには{}と{}がつきます".format(self.drink , self.food))
    def kaikei(self,kosu):
        kei = self.tanka * kosu
        print("{}セットのご注文なので合計{}円です".format(kosu , kei))


lunch = lunchset()
lunch.naiyou()
lunch.kaikei(3)