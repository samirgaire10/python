
IT = [88,90,95,100,99,92]

print('CD68期ISI7期の全点数 ={}'.format(IT))
print("うちCD６８期 点数={}".format(IT[:4] ))
print("うちIS１７期 点数={}".format(IT[-2:]))


print("CD68期合計{},平均は{}".format(sum(IT[:4]),  sum(IT[:4])/len(IT[:4])))

print("CD68期合計{},平均は{}".format(sum(IT[-2:]),  sum(IT[-2:])/len(IT[-2:])))

