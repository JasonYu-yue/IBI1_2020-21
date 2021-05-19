seq = 'ATGCGACTACGATCGAGGGCC'
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
protein=''
#recongnize the condon 
for i in range (0,len(seq),3):
    #detect the condon in the dictionary 
    codon=seq[i:i+3]
     #find its corresponded amino acid and add the amino acids to the protein sequence
    #transfer the key of the genetic code(condons) to thier values(amino acids)
    protein+=genetic_code [codon]
print(protein)


