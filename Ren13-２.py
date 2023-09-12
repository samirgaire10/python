
class chara:
    name  = "gaire samir"
    cm = '2000000000000'
    def syoukai(self):
        print("{}さんは身長{}cm".format(self.name , self.cm))
    def syoukai2(self,name2,cm2):
        print("{}さんは身長{}cm".format(name2 , cm2))


jinbutu = chara()
jinbutu.syoukai()
jinbutu.syoukai2('山本',199.8)
