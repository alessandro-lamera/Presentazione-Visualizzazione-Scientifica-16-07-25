import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Presentazione/Dataset/Nati serie storica.csv')
NomiRegioni=['Piemonte','Valle d\'Aosta / Vallée d\'Aoste','Liguria','Lombardia','Trentino Alto Adige / Südtirol','Veneto','Friuli-Venezia Giulia','Emilia-Romagna','Toscana','Umbria','Marche','Lazio','Abruzzo','Campania','Puglia','Basilicata','Calabria','Sardegna','Sicilia','Molise']
anno1= 2023
anno2=2013
anno3= 2003

dataframes1=[]
for x in NomiRegioni:
    nati= df[df['Territorio di residenza'].eq(x)]
    nati2= nati[nati['TIME_PERIOD'].eq(anno1)]
    dataframes1.append(nati2)

Frame1= pd.concat(dataframes1, ignore_index=True)
for x in Frame1.index:
    if Frame1.loc[x, 'RESIDENCE_TERR']==('ITC20'):
        Frame1.drop(x, inplace = True)

dataframes2=[]
for x in NomiRegioni:
    nati= df[df['Territorio di residenza'].eq(x)]
    nati2= nati[nati['TIME_PERIOD'].eq(anno2)]
    dataframes2.append(nati2)

Frame2= pd.concat(dataframes2, ignore_index=True)
for x in Frame2.index:
    if Frame2.loc[x, 'RESIDENCE_TERR']==('ITC20'):
        Frame2.drop(x, inplace = True)

dataframes3=[]
for x in NomiRegioni:
    nati= df[df['Territorio di residenza'].eq(x)]
    nati2= nati[nati['TIME_PERIOD'].eq(anno3)]
    dataframes3.append(nati2)

Frame3= pd.concat(dataframes3, ignore_index=True)
for x in Frame3.index:
    if Frame3.loc[x, 'RESIDENCE_TERR']==('ITC20'):
        Frame3.drop(x, inplace = True)

plt.figure(figsize=(12, 6))

plt.barh(Frame1['Territorio di residenza'], Frame1['Osservazione'], 
        color="#036FB7", 
        height =0.5, zorder=3, alpha=0.9,label=2023)

plt.barh(Frame2['Territorio di residenza'], Frame2['Osservazione'], 
        color="#0099FF", 
        height =0.5, zorder=2, alpha=0.8,label=2013)
plt.barh(Frame3['Territorio di residenza'], Frame3['Osservazione'], 
        color='skyblue', 
        height =0.5, zorder=1, alpha=0.8,label=2003)
    
plt.ylabel('Regioni',fontsize=11)
plt.xlabel('Nascituri',fontsize=11)
plt.xticks(fontsize=8)
plt.title("Confronto della natalità fra le regioni negli anni")
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.legend(loc = "upper center", bbox_to_anchor = (0.8, 1.0), fancybox = True, shadow = True)
plt.tight_layout()
plt.show()
