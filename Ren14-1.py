

class Character:
    name = "ライオン"
    setsumei = "百獣の王"
    def char_print(self):
        print("当動物園でおすすめ:{}".format(self.name))


print("処理科どうぶつえんへようこそ!")
animal  = Character()
animal.char_print()

print("PRポイント:{}".format(animal.setsumei))
