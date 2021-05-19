#build up a dictionary fro the principle of the base pairing
pairing={'A':'T','T':'A','G':'C','C':'G'}
#the input and the output of the function should be consistent
def pare(singleDNA):
    reverseDNA=''
    #define the reverse chain in function
    singleDNA=singleDNA.upper()
    for n in range (0,len(singleDNA)):
        reverseDNA+=pairing[singleDNA[n]]
    return reverseDNA
    #the content of reverseDNA return to the singleDNA
singleDNA='CATGCAagcTAgctAgT'
print(pare(singleDNA))

