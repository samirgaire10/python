
i = 0

score = [80,95,98,100]
print(score)

avg = sum(score) / len(score)
print("平均点は{}点です".format(avg))    

for avg in score:
    if avg <= score[i]: 
        print('{}組の得点{}点で平均点以上です'.format(i+1,score[i]))
        i = i+1
    else:
        print('{}組の得点{}点で平均点未満です'.format(i+1,score[i]))
        i = i+1 
