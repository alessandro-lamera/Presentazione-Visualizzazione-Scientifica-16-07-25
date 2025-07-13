import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Presentazione/Dataset/Bilancio_Demografico/Bilancio demografico 2019.csv')
dg = pd.read_csv('Presentazione/Dataset/Bilancio_Demografico/Bilancio demografico 2020.csv')
dh = pd.read_csv('Presentazione/Dataset/Bilancio_Demografico/Bilancio demografico 2021.csv')
di = pd.read_csv('Presentazione/Dataset/Bilancio_Demografico/Bilancio demografico 2022.csv')
dl = pd.read_csv('Presentazione/Dataset/Bilancio_Demografico/Bilancio demografico 2023.csv')
dm = pd.read_csv('Presentazione/Dataset/Bilancio_Demografico/Bilancio demografico 2024.csv')
death=[]
born=[]
death.append(df.at[2,"Totale"])
death.append(dg.at[2,"Totale"])
death.append(dh.at[2,"Totale"])
death.append(di.at[2,"Totale"])
death.append(dl.at[2,"Totale"])
death.append(dm.at[2,"Totale"])
born.append(df.at[1,"Totale"])
born.append(dg.at[1,"Totale"])
born.append(dh.at[1,"Totale"])
born.append(di.at[1,"Totale"])
born.append(dl.at[1,"Totale"])
born.append(dm.at[1,"Totale"])
time=[2019,2020,2021,2022,2023,2024]
plt.plot(time,death, alpha=0.8,color="#0099FF")
plt.plot(time,born, alpha=0.8,color= "skyblue")
plt.title("Ricambio Generazionale", fontsize=15)
plt.xlabel("Anni", fontsize=11)
plt.ylabel("Cittadini",fontsize=11)
mylabels=("Morti","Nascituri")
plt.legend(loc = "upper center", bbox_to_anchor = (0.85, 1.0), fancybox = True, shadow = True, labels= mylabels)
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.tight_layout()
plt.show()