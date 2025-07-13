import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Presentazione/Dataset/Bilancio_Demografico/Bilancio demografico 2019.csv')
dg = pd.read_csv('Presentazione/Dataset/Stranieri_In_Italia/Popolazione straniera residente 2019.csv')


popolazione=[]
totminus=df.at[13,"Totale"]-dg.at[101,"Totale"]
popolazione.append(totminus)
popolazione.append(dg.at[101,"Totale"])

labels =["Popolazione locale: 91,62%", "Stranieri: 8,38%"]
labels_indexes = np.arange(len(labels))
myexplode= [0, 0.2]
plt.figure(figsize=(9,7))
mycolors = ["#0099FF","skyblue"]
plt.pie(popolazione, startangle = 50, explode = myexplode,shadow = None, colors=mycolors,wedgeprops = {"alpha": 0.8})

plt.legend(loc = "upper center", bbox_to_anchor = (0.93, 0.01, 0.20, 0.95), fancybox = True, shadow = True, labels= labels)
plt.title("Contributo degli stranieri al totale della popolazione nel 2019", x=0.5, y=0.97, fontsize=15)
plt.tight_layout()
plt.show()

