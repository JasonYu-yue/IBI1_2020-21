Gh=open('SOD2_human.fa')
Gm=open('SOD2_mouse.fa')
Gr=open('RandomSeq.fa')
import re
identical_distance= 0
persentage = 0
seq1 = ""
seq2 = ""
seq3 = ""
#I got some help from classmate Tang Shijie and Hu Zihao
#I I use their ideas to complete my code
for line in Gr:
  if re.search(r'>',line):
   Rname = re.findall(r'>(.+?)$', line)
  else:
   seq1 = line.strip()
   #these steps are used to get the dna sequence
for line in Gh:
  if re.search(r'>',line):
   Hname = re.findall(r'>(.+?)$', line)
  else:
   seq2 = line.strip()
for line in Gm:
  if re.search(r'>',line):
   Mname = re.findall(r'>(.+?)$', line)
  else:
   seq3 = line.strip()
#the following steps are used to calculate the score of the deiffenerce
#and the percentage of 
for i in range(len(seq1)):
  if seq1[i] == seq2[i]:
   identical_distance += 1
percentage = (identical_distance / len(seq1)) * 100
print("the identical_distance score of human-Randome is : " + str(identical_distance))
print("the persentage is : " + str(percentage) + "%")
identical_distance = 0
for n in range(len(seq1)):
  if seq1[n] == seq3[n]:
   identical_distance +=1
percentage = (identical_distance / len(seq1)) * 100
print("the identical_distance score of mouse-Randome is : " + str(identical_distance))
print("the persentage is : " + str(percentage) + "%")
identical_distance = 0
for n in range(len(seq2)):
  if seq2[n] == seq3[n]:
   identical_distance +=1
percentage = (identical_distance / len(seq1)) * 100
print("the identical_distance score of mouse-human is : " + str(identical_distance))
print("the persentage is : " + str(percentage) + "%")