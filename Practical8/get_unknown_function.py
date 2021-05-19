#open the file in the reading form
data = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
import re
gene=' '
result=' '
a = False
#use a to identify whether there exsits "unknown function" in the line
seq = ''
for line in data:
 if re.search(r'>',data):
  if a == True:
   result = result+ (gene+'     '+ str(len(seq))+ '\n' + seq + '\n')
   #add the gene name, the length and the sequence to the result
   seq = ''
   gene = ''
   #clear the gene name and sequence in order to add new gene type in the next count
   a = False
  if re.findall(r'unknown.function', line):
   gene = re.findall(r'^>(Y.+?$)', line)
   #find out the gene name since gene name begin with "Y"
   gene = gene[0]
   a = True
 else:
  if a == True:
   seq = seq +line.strip()
   #add the unknown gene line by line
data.close()
#creat a new file in writing form
outcome = open('unknown_function.fa','w')
outcome.write(result)
outcome.close()