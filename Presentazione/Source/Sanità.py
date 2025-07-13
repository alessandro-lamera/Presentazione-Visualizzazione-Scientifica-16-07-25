import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Presentazione/Dataset/Foi medie annue dal 2016.csv')

sanità=df[df["ECOICOP Rev. Istat"].eq("-- servizi sanitari e spese per la salute")] 
plt.figure(figsize=(10, 6))
plt.plot(sanità["TIME_PERIOD"],sanità["Osservazione"], alpha=0.7, marker='o', linestyle='-', color='royalblue', linewidth=2)
plt.title("INFLAZIONE SANITA'",fontsize=16, fontweight='bold')
plt.xlabel("Anni", fontsize=12)
plt.ylabel("Costo della sanità",fontsize=12)
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.tight_layout()
plt.show()