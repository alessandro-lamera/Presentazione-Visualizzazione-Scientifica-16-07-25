import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset1 = pd.read_csv("Presentazione/Dataset/Demografia_Genitori/Età media delle madri al parto per anno di evento e cittadinanza della madre.csv")
dataset2 = pd.read_csv("Presentazione/Dataset/Demografia_Genitori/Età media dei padri alla nascita del figlio.csv")
Padri= dataset2[dataset2["Territorio"].eq("Italia")]
Madri=dataset1[dataset1["Territorio"].eq("Italia")]
plt.figure(figsize=(8,5))
mylabels=("Padri","Madri")
plt.xlabel("Anni", fontsize=11)
plt.ylabel("Età media dei genitori", fontsize=11)
plt.plot(Padri["TIME_PERIOD"],Padri["Osservazione"], alpha=0.8,color="#0099FF")
plt.plot(Madri["TIME_PERIOD"],Madri["Osservazione"], color='skyblue',alpha=0.8,)
plt.legend(loc = "upper center", bbox_to_anchor = (0.09, 0.97), fancybox = True, shadow = True, labels= mylabels)
plt.xticks(np.arange(1999,2024,4))
plt.yticks(np.arange(30,37,1))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.title("Variazione dell'età media dei genitori negli anni", fontsize=15)
plt.tight_layout()
plt.show()