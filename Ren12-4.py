"""


class Hero:
    name = "山本"
    hp = 100
    def sleep(self,hour):
        print("{}は{}時間寝た！".format(self.name,hour))
        self.hp += hour



print("*** 処理科ファンタジー II***")
h = Hero()
print("{}のHPは現在{}です".format(h.name,h.hp))
h.sleep(10)
print("{}のHPは現在{}です".format(h.name,h.hp))