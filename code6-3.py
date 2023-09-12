"""

ueseinfo = input("名前と血液型をカンマで区切って１行で入力＞＞")
[name, blood ] = ueseinfo.split(',')
blood = blood.upper().strip()
print("{}さん{}型なので大吉です".format(name,blood))