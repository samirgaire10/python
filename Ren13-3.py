
class keisan:
    name  = "gaire samir"
    tosi = 99999999999
    def keisan(self,after):
        goukei = self.tosi +  after
        print("現在{}歳の{}は,2026年には{}歳になります ".format(self.tosi , self.name, goukei))


obj  = keisan()
nengo = 2026 - 2023
obj.keisan(nengo)
