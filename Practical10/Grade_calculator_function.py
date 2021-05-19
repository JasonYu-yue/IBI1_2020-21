 #prepare for the input
name=input('studentname')
poster=input('score1')
code=input('score2')
final=input('score3')
#creat the function
def score():
    #calculate
    score=0.3*float(poster)+0.3*float(code)+0.4*float(final)
    #return the score to the initial place
    return score
print('student name'+':'+str(score))

#example
studentname='Yu Yue'
score1='90'
score2='88'
score3='86'