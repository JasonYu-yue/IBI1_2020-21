#start an empty dictionary
my_dict={}
#list the key and value
countries={'USA':29862124,'India':11285561,'Brazil':112059}
import matplotlib.pyplot as plt
labels='USA','India','Brazil','Russia','UK'
sizes=[29862124,11285561,11205972,4360823,4234924]
explode=(0.1,0,0,0,0)
#specifies the fraction of the radius with which to offset each wedge
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
#Equal aspect ratio ensures that pie is drawn as a cricle
plt.show()