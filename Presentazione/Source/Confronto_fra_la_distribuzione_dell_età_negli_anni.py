import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

persone = pd.read_csv("Presentazione/Dataset/Popolazione_Residente/Popolazione residente 2019.csv")
persone2 = pd.read_csv("Presentazione/Dataset/Popolazione_Residente/Popolazione residente 2024.csv")
limitsx=0
limitdx=9
spazio=0.20
UltimoDato= persone.at[100,"Totale"]
persone['Età'] = pd.to_numeric(persone['Età'], errors='coerce')
persone["Totale"]=pd.to_numeric(persone["Totale"], errors='coerce')
FrequenzeEtà = []

while limitdx<= 99:
    Frequenza_Età_Dataset= persone[(persone["Età"]<= limitdx) & (persone["Età"]>= limitsx)]
    FrequenzeEtà.append(pd.to_numeric(Frequenza_Età_Dataset["Totale"].sum()))
    limitdx= limitdx+10
    limitsx= limitsx+10
FrequenzeEtà.append(UltimoDato)   

labels =["0-9", "10-19", "20-29", "30-39", "40-49","50-59", "60-69", "70-79","80-89", "90-99", "100 e oltre"]
labels_indexes = np.arange(len(labels))
plt.figure(figsize=(8,4))
plt.barh(labels_indexes-spazio, FrequenzeEtà, height=0.4,label=2019, color="#0099FF", alpha= 0.8, zorder=2)
plt.xticks(fontsize=7.3)
plt.title("Confronto fra le fasce d'età della popolazione italiana negli anni", fontsize=12)
plt.xticks(np.arange(0,10000000,1000000))
plt.ticklabel_format(axis='x', style="plain")
plt.xlabel("Persone", fontsize=11)
plt.ylabel("Età", fontsize=11)
plt.yticks(labels_indexes,labels)
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')

limitsx2=0
limitdx2=9

UltimoDato2= persone2.at[100,"Totale"]
persone2['Età'] = pd.to_numeric(persone2['Età'], errors='coerce')
persone2["Totale"]=pd.to_numeric(persone2["Totale"], errors='coerce')
FrequenzeEtà2 = []

while limitdx2<= 99:
    Frequenza_Età_Dataset2= persone2[(persone2["Età"]<= limitdx2) & (persone2["Età"]>= limitsx2)]
    FrequenzeEtà2.append(pd.to_numeric(Frequenza_Età_Dataset2["Totale"].sum()))
    limitdx2= limitdx2+10
    limitsx2= limitsx2+10
FrequenzeEtà2.append(UltimoDato2)

plt.barh(labels_indexes+spazio, FrequenzeEtà2, height=0.4,label=2024, color="skyblue",alpha=0.8, zorder=1)
plt.legend(loc = "upper center", bbox_to_anchor = (0.8, 1.0), fancybox = True, shadow = True)
plt.tight_layout()
plt.show()
