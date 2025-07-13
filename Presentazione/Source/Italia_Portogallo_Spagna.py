import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Presentazione/Dataset/Nascite in europa.csv')
NuovoDataset= df[ (df['geo'].eq("Portugal")) |  (df['geo'].eq("Spain")) | (df['geo'].eq("Italy"))]
spazio= 0.20
Portugal= NuovoDataset[df['geo'].eq("Portugal")]
Spain= NuovoDataset[df['geo'].eq("Spain")]
Italy= NuovoDataset[df['geo'].eq("Italy")]

plt.figure(figsize=(12,6))
plt.subplot(1, 2, 1)
plt.bar( Portugal["TIME_PERIOD"]-spazio, Portugal["OBS_VALUE"],width=0.4,zorder=2,  color='#0099FF', alpha=0.8)
plt.bar( Italy["TIME_PERIOD"]+spazio, Italy["OBS_VALUE"], width=0.4,zorder=3, color='skyblue', alpha=0.8)
plt.xlabel("Anni")
plt.ylabel("Nascituri")
plt.xticks(fontsize=8)
plt.xticks(np.arange(2012,2024,1))
mylabels1=("Portogallo","Italia")
plt.legend(loc = "upper center", bbox_to_anchor = (0.85, 1.0), fancybox = True, shadow = True, labels= mylabels1)
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')


plt.subplot(1, 2, 2)
plt.bar( Spain["TIME_PERIOD"]-spazio, Spain["OBS_VALUE"],width=0.4, zorder= 2,  color='#0099FF', alpha=0.8)
plt.bar( Italy["TIME_PERIOD"]+spazio, Italy["OBS_VALUE"], width=0.4,zorder=3, color='skyblue', alpha=0.8)
plt.xlabel("Anni")
plt.ylabel("Nascituri")
plt.xticks(fontsize=8)
plt.xticks(np.arange(2012,2024,1))
mylabels=("Spagna","Italia")
plt.legend(loc = "upper center", bbox_to_anchor = (0.85, 1.0), fancybox = True, shadow = True, labels= mylabels)
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')

plt.suptitle("Confronto sull'andamento demografico fra L'italia, la Spagna e il Portogallo",fontsize=15)
plt.tight_layout()
plt.show()