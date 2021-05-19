#make a list about the counted gene
gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
import numpy as np
a=np.array(gene_lengths)
b=np.array(exon_counts)
a/b
L=a/b
L=sorted(L)
L
# rectangular box plot
import numpy as np
import matplotlib.pyplot as plt
#I obtained the code from IBI week6 lecture
n=10
score=np.random.uniform(3.8898964128730826,842,n)
plt.boxplot(score,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False
            )  
plt.ylabel('length')
plt.show()
