ten = []
ten.append(int(input("1人の点数：")))
ten.append(int(input("2人の点数：")))
ten.append(int(input("3人の点数：")))

total = sum(ten)
avg = total / len(ten)

print("合計{}点です".format(total))
print("合計{}点です".format(avg))

print("1人目の点数は{}点、平均との表{}点".format(ten[0], ten[0]-avg ))
print("1人目の点数は{}点、平均との表{}点".format(ten[1], ten[1]-avg ))
print("1人目の点数は{}点、平均との表{}点".format(ten[2], ten[2]-avg ))


  

 
