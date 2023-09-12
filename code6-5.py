"""


class Hero:
    name = "松田"
    hp = 100
    def sleep(self,hour):
        print("{}は{}時間寝た！".format(self.name,hour))
        self.hp += hour



print("スッキリファンタジーXII〜金色の理想郷")
h = Hero()
h.sleep(3)
print("{}のHPは現在{}です".format(h.name,h.hp))