import numpy as np
import matplotlib.pyplot as plt
#DATA
country=['INDIA','JAPAN','MEXICO','COLOMBIA','GERMANY']
population=[1000,800,900,1200,300]

#CREAR GRAFICO

plt.bar(country,population,width=0.5,color=['red'])
plt.xticks(np.arange(5),('India','Japon','Mexico','Colombia','Alemania'),rotation=20)
plt.show()
