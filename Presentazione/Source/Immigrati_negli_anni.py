import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Presentazione/Dataset/Bilancio_Demografico/Bilancio demografico 2019.csv')
dg = pd.read_csv('Presentazione/Dataset/Bilancio_Demografico/Bilancio demografico 2020.csv')
dh = pd.read_csv('Presentazione/Dataset/Bilancio_Demografico/Bilancio demografico 2021.csv')
di = pd.read_csv('Presentazione/Dataset/Bilancio_Demografico/Bilancio demografico 2022.csv')
dl = pd.read_csv('Presentazione/Dataset/Bilancio_Demografico/Bilancio demografico 2023.csv')
dm = pd.read_csv('Presentazione/Dataset/Bilancio_Demografico/Bilancio demografico 2024.csv')

popolazione=[]
time=[2019,2020,2021,2022,2023,2024]

popolazione.append(df.at[7,"Totale"])
popolazione.append(dg.at[7,"Totale"])
popolazione.append(dh.at[7,"Totale"])
popolazione.append(di.at[7,"Totale"])
popolazione.append(dl.at[7,"Totale"])
popolazione.append(dm.at[7,"Totale"])

plt.plot(time,popolazione, c='#0099FF', alpha=0.8)
plt.title("Andamento dell'immigrazione negli anni", fontsize=15)
plt.xlabel("Anni", fontsize=11)
plt.ylabel("Immigrati", fontsize=11)
plt.ticklabel_format(axis='both', style="plain")
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.tight_layout()
plt.show()