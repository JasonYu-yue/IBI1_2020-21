#creat a dictionary that contains the principle for DNA_to_protein
#choose the three letter nucleotides as keys, and the related amino acids as values 
genetic_code={ 'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
    'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
    'ATT':'I','ATC':'I','ATA':'J','ATG':'M',
    'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
    'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
    'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
    'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
    'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
    'TAT':'Y','TAC':'Y','TAA':'','TAC':'',
    'CAT':'H','CAC':'H','CAA':'Q','CAG':'Z',
    'AAT':'N','AAC':'B','AAA':'K','AAG':'K',
    'GAT':'D','GAC':'D','GAA':'E','GAG':'E',
    'TGT':'C','TGC':'C','TGA':'','TGG':'W',
    'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
    'AGT':'S','AGC':'S','AGA':'R','AGG':'R',
    'GGT':'G','GGC':'G','GGA':'G','GGG':'G'}
#establish the protein sequence
gene=input('Please input the file name :')
protein=''
#open the file in the reading form
data = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
import re
name=' '
result=' '
a = False
#use a to identify whether there exsits "unknown function" in the line
seq = ''
for line in data:
 if re.search(r'>',data):
  if a == True:
      for i in range (0,len(gene),3):
          codon=gene[i:i+3]
          protein+=genetic_code [codon]
    #detect the condon in the dictionary 
    #find its corresponded amino acid and add the amino acids to the protein sequence
    #transfer the key of the genetic code(condons) to thier values(amino acids)
      result = result+ (name+'     '+ str(len(seq))+ '\n' + seq + '\n')
   #add the gene name, the length and the sequence to the result
      seq = ''
      name = ''
   #clear the gene name and sequence in order to add new gene type in the next count
      protein=''
      a = False
  if re.findall(r'unknown.function', line):
   name = re.findall(r'^>(Y.+?$)', line)
   #find out the gene name since gene name begin with "Y"
   name = name[0]
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