import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Presentazione/Dataset/Nascite in europa.csv')
NuovoDataset= df[ (df['geo'].eq("Germany")) |  (df['geo'].eq("France")) | (df['geo'].eq("Italy"))]
spazio= 0.20
Germany= NuovoDataset[df['geo'].eq("Germany")]
France= NuovoDataset[df['geo'].eq("France")]
Italy= NuovoDataset[df['geo'].eq("Italy")]
plt.figure(figsize=(12,6))
plt.subplot(1, 2, 1)
plt.bar( Germany["TIME_PERIOD"]-spazio, Germany["OBS_VALUE"],width=0.4,zorder=2, color='#0099FF', alpha=0.8)
plt.bar( Italy["TIME_PERIOD"]+spazio, Italy["OBS_VALUE"], width=0.4,zorder=3, color='skyblue', alpha=0.8)
plt.xlabel("Anni")
plt.ylabel("Nascituri")
plt.xticks(fontsize=8)
plt.xticks(np.arange(2012,2024,1))
mylabels1=("Germania","Italia")
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.legend(loc = "upper center", bbox_to_anchor = (0.15, 1.0), fancybox = True, shadow = True, labels= mylabels1)


plt.subplot(1, 2, 2)
plt.bar( France["TIME_PERIOD"]-spazio, France["OBS_VALUE"],width=0.4, color='#0099FF', alpha=0.8,zorder= 2)
plt.bar( Italy["TIME_PERIOD"]+spazio, Italy["OBS_VALUE"], width=0.4, color='skyblue', alpha=0.8,zorder=3  )
plt.xlabel("Anni")
plt.ylabel("Nascituri")
plt.xticks(fontsize=8)
plt.xticks(np.arange(2012,2024,1))
mylabels=("Francia","Italia")
plt.legend(loc = "upper center", bbox_to_anchor = (0.85, 1.0), fancybox = True, shadow = True, labels= mylabels)
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')

plt.suptitle("Confronto sull'andamento demografico fra L'italia, la Germania e la Francia", fontsize=15)
plt.tight_layout()
plt.show()