import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Presentazione/Dataset/Nati serie storica.csv')
etichetta= 'IT'

nuove_nascite= df[df['RESIDENCE_TERR'].eq(etichetta)]
nuove_nascite.plot(x = 'TIME_PERIOD', y = 'Osservazione', label='Nascite', color="#0099FF", alpha=0.8)

plt.title("Nuove nascite dal 1999 al 2023", fontsize= 15)
plt.xticks(np.arange(1999,2024,4))
plt.xlabel("Anni", fontsize=12)
plt.ylabel("Nuove Nascite", fontsize=12)
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.tight_layout()
plt.show()