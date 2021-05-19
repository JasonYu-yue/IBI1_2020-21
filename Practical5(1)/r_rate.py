# define variables for student number and the infection rate
# n represent the times of infection 
a = 84
r = 1.1
n = 1
# the infection can be culculated by for-loop.
for n in range(1,6) :
 a = a + a*r
 n = n+1
# print the result
a = str(a)
r = str(r)
print ("r = "+ r)
print ("the infection number is "+ a)
