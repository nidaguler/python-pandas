import pandas as pd

dictionary={"Ad":["Zed","Yasuo","Malphite","Garen","Zilean"],
            "Yas":[21,22,23,24,25],
            "Maas":[1500,1600,1700,1800,1900],
            "Boy":[160,170,180,190,200]}
dataframe1=pd.DataFrame(dictionary)

#ortalama maasi bulalim
ortalama_maas=dataframe1.Maas.mean() #mean() metodu ortalama bulmamizi saglar.
print(ortalama_maas)
#sonuc
"""
1700.0
"""
#bunu numpyda nasil yaptigimiza bakalim
#import numpy as np
#ortalama_maas_np=np.mean(dataframe1.Maas)
##sonuc
#"""
#1700.0
#"""

#simdi dataframemimize yeni bi kolon ekleyelim ve maas ortalamasina gore seviye belirleyelim.

dataframe1["maas_seviyesi"]=["dusuk" if ortalama_maas > each else "yuksek" for each in dataframe1.Maas] #list comprehension

#normalde yaptigimiz sekli asagidaki gibi
for each in dataframe1.Maas:
    if ortalama_maas > each:
        print("dusuk")
    else:
            print("yuksek")
            

#bize daginik, kotu yazilmis bi data gelirse diye duzeltmek icin mesela butun kolon adlarini kucuk harfe cevirelim

dataframe1.columns=[each.lower() for each in dataframe1.columns]
print(dataframe1.columns)
#sonuc
"""
Index(['ad', 'yas', 'maas', 'boy', 'maas_seviyesi'], dtype='object')
"""
#simdi yeni bir kolon ekleyelim ve adinda bosluk olsun

dataframe1["yeni kolon"]=[200,300,400,500,600]

#simdi de boyle bosluklu kolon adlarini gordugumuzde birlestirmesi icin bir list comprehension yapalim


dataframe1.columns = [each.split()[0]+"_"+each.split()[1] if (len(each.split())>1) else each for each in dataframe1.columns]
print(dataframe1.columns)
#sonuc
"""
dataframe1.columns = ifadesini tek tek konusalim
1) for each ifadesiyle butun kolon adlarını donmesini soyluyoruz.
2) if ifadesiyle  eger kolon adı uzunlugu 1den fazlaysa yani 2 kelimeyse 
    each.split()[0] yani yeni kolon ismindeki 1. kelime yeni kelimesi ile each.split()[1] kolon kelimesi arasina alt cizgi koy demis olduk
else ifadesiyle de eger iki kelime veya fazla değilse yanitek kelimeyse bize direkt kolon adini dondurmesini soyluyoruz.


Index(['ad', 'yas', 'maas', 'boy', 'maas_seviyesi', 'yeni_kolon'], dtype='object')
"""