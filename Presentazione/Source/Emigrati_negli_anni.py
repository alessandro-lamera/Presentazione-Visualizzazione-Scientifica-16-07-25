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

popolazione.append(df.at[8,"Totale"])
popolazione.append(dg.at[8,"Totale"])
popolazione.append(dh.at[8,"Totale"])
popolazione.append(di.at[8,"Totale"])
popolazione.append(dl.at[8,"Totale"])
popolazione.append(dm.at[8,"Totale"])

plt.plot(time,popolazione, c='blue')
plt.title("Andamento dell'Emmigrazione negli anni")
plt.xlabel("Anni")
plt.ylabel("Emigrati")
plt.ticklabel_format(axis='both', style="plain")
plt.tight_layout()
plt.show()