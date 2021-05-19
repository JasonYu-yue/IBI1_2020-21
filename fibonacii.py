#Function: calculate the 13th number in fibonacci series
#a=1
#b=1
#Reapeat:
#a=a+b
#b=b+a
#How many times?
# If less than 11: keep on
# If 11:Done!
a=1
b=1
count=11
for i in range(1,12):
 if count%2==1:
  a=a+b
 else:
  b=b+a
 count=count-1
 if count==0:
    if a>b:
     print(a)
    else:
     print(b)
#print the max value of {a,b} as the 13th number in fibonacci series


#Function:list the first 13th number in fibonacci series
a=1
b=1
for i in range(1,12):
 if count%2==1:
  a=a+b
  print(a)
 else:
  b=b+a
  print(b)
 count=count-1
