"""

def kake(x , y):
    answer = x * y 
    return answer


def wari(x , y):
    answer = x / y 
    return answer


print("計算を行います")


check =  input("かけ算はaまたはA、わり算はbまたはBを入力>>A  :")

if check == 'A' or check == 'a':
    x= int(input("1つめのオペランド>> "))
    y= int(input("2つめのオペランド>>"))
    answer = kake(x,y)
    print("かけ算の答え{}".format(answer))


if check == 'B' or check == 'b':
    x= int(input("1つめのオペランド>>"))
    y= int(input("2つめのオペランド>>"))
    answer =wari(x,y)
    print("わり算の答え{}".format(answer))
