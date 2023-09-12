
class lunchset:
    drink = "コーヒー"
    food = 'サンドイッチ'
    def kaiten(self):
        print("いらっしゃいませ!")
        print("ランチセットには{}と{}がつきます".format(self.drink , self.food))

lunch = lunchset()
lunch.kaiten()