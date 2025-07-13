import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv("Presentazione/Dataset/Popolazione_Residente/Popolazione residente Gennaio 2025.csv")
persone = dataset[dataset["Sesso"].eq("Totale")]
FrequenzeEtà = []
array1=["Y0","Y1","Y2","Y3","Y4","Y5","Y6","Y7","Y8","Y9"]
array2=["Y10","Y11","Y12","Y13","Y14","Y15","Y16","Y17","Y18","Y19"]
array3=["Y20","Y21","Y22","Y23","Y24","Y25","Y26","Y27","Y28","Y29"]
array4=["Y30","Y31","Y32","Y33","Y34","Y35","Y36","Y37","Y38","Y39"]
array5=["Y40","Y41","Y42","Y43","Y44","Y45","Y46","Y47","Y48","Y49"]
array6=["Y50","Y51","Y52","Y53","Y54","Y55","Y56","Y57","Y58","Y59"]
array7=["Y60","Y61","Y62","Y63","Y64","Y65","Y66","Y67","Y68","Y69"]
array8=["Y70","Y71","Y72","Y73","Y74","Y75","Y76","Y77","Y78","Y79"]
array9=["Y80","Y81","Y82","Y83","Y84","Y85","Y86","Y87","Y88","Y89"]
array10=["Y90","Y91","Y92","Y93","Y94","Y95","Y96","Y97","Y98","Y99"]

Frequenza_Età_Dataset1= persone[(persone["AGE"].eq(array1[0])) | (persone["AGE"].eq(array1[1])) |(persone["AGE"].eq(array1[2])) | (persone["AGE"].eq(array1[3])) | (persone["AGE"].eq(array1[4])) | (persone["AGE"].eq(array1[5])) | (persone["AGE"].eq(array1[6])) | (persone["AGE"].eq(array1[7])) | (persone["AGE"].eq(array1[8])) | (persone["AGE"].eq(array1[9]))]
FrequenzeEtà.append(pd.to_numeric(Frequenza_Età_Dataset1["Osservazione"].sum()))

Frequenza_Età_Dataset2= persone[(persone["AGE"].eq(array2[0])) | (persone["AGE"].eq(array2[1])) |(persone["AGE"].eq(array2[2])) | (persone["AGE"].eq(array2[3])) | (persone["AGE"].eq(array2[4])) | (persone["AGE"].eq(array2[5])) | (persone["AGE"].eq(array2[6])) | (persone["AGE"].eq(array2[7])) | (persone["AGE"].eq(array2[8])) | (persone["AGE"].eq(array2[9])) ]
FrequenzeEtà.append(pd.to_numeric(Frequenza_Età_Dataset2["Osservazione"].sum()))

Frequenza_Età_Dataset3= persone[(persone["AGE"].eq(array3[0])) | (persone["AGE"].eq(array3[1])) |(persone["AGE"].eq(array3[2])) | (persone["AGE"].eq(array3[3])) | (persone["AGE"].eq(array3[4])) | (persone["AGE"].eq(array3[5])) | (persone["AGE"].eq(array3[6])) | (persone["AGE"].eq(array3[7])) | (persone["AGE"].eq(array3[8])) | (persone["AGE"].eq(array3[9]))]
FrequenzeEtà.append(pd.to_numeric(Frequenza_Età_Dataset3["Osservazione"].sum()))

Frequenza_Età_Dataset4= persone[(persone["AGE"].eq(array4[0])) | (persone["AGE"].eq(array4[1])) |(persone["AGE"].eq(array4[2])) | (persone["AGE"].eq(array4[3])) | (persone["AGE"].eq(array4[4])) | (persone["AGE"].eq(array4[5])) | (persone["AGE"].eq(array4[6])) | (persone["AGE"].eq(array4[7])) | (persone["AGE"].eq(array4[8])) | (persone["AGE"].eq(array4[9])) ]
FrequenzeEtà.append(pd.to_numeric(Frequenza_Età_Dataset4["Osservazione"].sum()))

Frequenza_Età_Dataset5= persone[(persone["AGE"].eq(array5[0])) | (persone["AGE"].eq(array5[1])) |(persone["AGE"].eq(array5[2])) | (persone["AGE"].eq(array5[3])) | (persone["AGE"].eq(array5[4])) | (persone["AGE"].eq(array5[5])) | (persone["AGE"].eq(array5[6])) | (persone["AGE"].eq(array5[7])) | (persone["AGE"].eq(array5[8])) | (persone["AGE"].eq(array5[9]))  ]
FrequenzeEtà.append(pd.to_numeric(Frequenza_Età_Dataset5["Osservazione"].sum()))

Frequenza_Età_Dataset6= persone[(persone["AGE"].eq(array6[0])) | (persone["AGE"].eq(array6[1])) |(persone["AGE"].eq(array6[2])) | (persone["AGE"].eq(array6[3])) | (persone["AGE"].eq(array6[4])) | (persone["AGE"].eq(array6[5])) | (persone["AGE"].eq(array6[6])) | (persone["AGE"].eq(array6[7])) | (persone["AGE"].eq(array6[8])) | (persone["AGE"].eq(array6[9]))  ]
FrequenzeEtà.append(pd.to_numeric(Frequenza_Età_Dataset6["Osservazione"].sum()))

Frequenza_Età_Dataset7= persone[(persone["AGE"].eq(array7[0])) | (persone["AGE"].eq(array7[1])) |(persone["AGE"].eq(array7[2])) | (persone["AGE"].eq(array7[3])) | (persone["AGE"].eq(array7[4])) | (persone["AGE"].eq(array7[5])) | (persone["AGE"].eq(array7[6])) | (persone["AGE"].eq(array7[7])) | (persone["AGE"].eq(array7[8])) | (persone["AGE"].eq(array7[9]))  ]
FrequenzeEtà.append(pd.to_numeric(Frequenza_Età_Dataset7["Osservazione"].sum()))

Frequenza_Età_Dataset8= persone[(persone["AGE"].eq(array8[0])) | (persone["AGE"].eq(array8[1])) |(persone["AGE"].eq(array8[2])) | (persone["AGE"].eq(array8[3])) | (persone["AGE"].eq(array8[4])) | (persone["AGE"].eq(array8[5])) | (persone["AGE"].eq(array8[6])) | (persone["AGE"].eq(array8[7])) | (persone["AGE"].eq(array8[8])) | (persone["AGE"].eq(array8[9])) ]
FrequenzeEtà.append(pd.to_numeric(Frequenza_Età_Dataset8["Osservazione"].sum()))

Frequenza_Età_Dataset9= persone[(persone["AGE"].eq(array9[0])) | (persone["AGE"].eq(array9[1])) |(persone["AGE"].eq(array9[2])) | (persone["AGE"].eq(array9[3])) | (persone["AGE"].eq(array9[4])) | (persone["AGE"].eq(array9[5])) | (persone["AGE"].eq(array9[6])) | (persone["AGE"].eq(array9[7])) | (persone["AGE"].eq(array9[8])) | (persone["AGE"].eq(array9[9]))  ]
FrequenzeEtà.append(pd.to_numeric(Frequenza_Età_Dataset9["Osservazione"].sum()))

Frequenza_Età_Dataset10= persone[(persone["AGE"].eq(array10[0])) | (persone["AGE"].eq(array10[1])) |(persone["AGE"].eq(array10[2])) | (persone["AGE"].eq(array10[3])) | (persone["AGE"].eq(array10[4])) | (persone["AGE"].eq(array10[5])) | (persone["AGE"].eq(array10[6])) | (persone["AGE"].eq(array10[7])) | (persone["AGE"].eq(array10[8])) | (persone["AGE"].eq(array10[9]))]
FrequenzeEtà.append(pd.to_numeric(Frequenza_Età_Dataset10["Osservazione"].sum()))

UltimoDato= dataset.at[304,"Osservazione"]
FrequenzeEtà.append(UltimoDato)   

y=[FrequenzeEtà[0]+FrequenzeEtà[1],FrequenzeEtà[2]+FrequenzeEtà[3],FrequenzeEtà[4]+FrequenzeEtà[5],FrequenzeEtà[6]+FrequenzeEtà[7],FrequenzeEtà[8]+FrequenzeEtà[9]]

#labels =["0-9", "10-19", "20-29", "30-39", "40-49","50-59", "60-69", "70-79","80-89", "90-99", "100 e oltre"]
labels =["0-19 anni: 16,88%", "20-39 anni: 21,37%", "40-59 anni: 29,52%", "60-79 anni: 24,48%","80-100 e oltre anni: 7,75%"]
labels_indexes = np.arange(len(labels))
#myexplode= [0, 0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.5]
myexplode= [0.1, 0.1, 0.1, 0.1, 0.1]
plt.figure(figsize=(9,7))
mycolors = ["blue","#036FB7","#0099FF","skyblue","cyan"]
plt.pie(y, startangle = 50, explode = myexplode,shadow = None, colors=mycolors ,wedgeprops = {"alpha": 0.7})
plt.legend(title = "Intervalli d'età (20 anni)",loc = "upper center", bbox_to_anchor = (0.93, 0.03, 0.20, 0.95), fancybox = True, shadow = True, labels= labels)
plt.title("Distribuzione per età della popolazione italiana nel 2025", x=0.5, y=0.97, fontsize=15)
plt.tight_layout()
plt.show()
