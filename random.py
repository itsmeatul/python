import random
def GetAnswer(answerNumber):
if answerNumber == 1:
return 'its one : you are luky fellow'
else if answerNumber == 2:
return 'its two : you are more than lucky'
else if answerNumber == 3:
return 'its three : you are 2 step ahead of luck'
else if answerNumber == 4:
return 'you are 4time lucky'
else if answerNumber == 5:
return 'you are 5times lucky'
else if answerNumber == 6:
return 'you are 6times lucky'
else if answerNumber == 7:
return 'you are 7times lucky'
else if answerNumber == 8:
return 'you are 8times lucky'
 elif answerNumber == 9:
           return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
