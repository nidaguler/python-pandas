import pandas as pd

dictionary= {"Ad":["ashe","lux","morgana","pyke","brand","blitzcrank"],

             "Yas":[23,24,25,26,27,28],

             "Maas":[1550,1450,1600,1800,1900,2000]}



dataframe1=pd.DataFrame(dictionary)
print(dataframe1["Ad"])#dataframeden sadece adlari ceker.
#sonuc
"""
*sayilar bulunduklari indexleri gosterir.
0          ashe
1           lux
2       morgana
3          pyke
4         brand
5    blitzcrank
"""
#baska bir yontem olarak kolon adiyla kullanimi
print(dataframe1.Yas)#yaslari verir
#sonuc
"""
*sayilar bulunduklari indexleri gosterir.
0    23
1    24
2    25
3    26
4    27
5    28
"""
#yeni feature=ad,yas,maas vs ekleme
#yeni feature olustururken bosluklu ad koymayin
dataframe1["Boy"]=[150,160,170,180,190,200]

print(dataframe1.loc[:,"Maas"])#tum satirlari : isareti ile aliyoruz ve maas olarak belirttigimiz sutunu cekiyoruz.
#sonuc
"""
0    1550
1    1450
2    1600
3    1800
4    1900
5    2000
"""
#belirtilen kadar secim yapma
print(dataframe1.loc[:3,"Maas"])#3 sayisi numpyda ve listte exclusive yani dahil değil iken pandasta dahil demektir. 0,1,2,3 indexlerine sahip elemanlari ceker. 
#sonuc
"""
0    1550
1    1450
2    1600
3    1800
"""
print(dataframe1.loc[:3,"Yas":"Boy"])#butun satirlari ve 0,1,2,3 indexlerine sahip elemanlari, yas ve boy dahil cekelim.
#sonuc
"""
   Yas  Maas  Boy
0   23  1550  150
1   24  1450  160
2   25  1600  170
3   26  1800  180
"""
#Yukaridaki yas ve boy arasina : koymustuk simdi virgul koyup farki gorelim
print(dataframe1.loc[:3,["Yas","Boy"]])
#sonuc
"""
   Yas  Boy
0   23  150
1   24  160
2   25  170
3   26  180
"""
print(dataframe1.loc[::-1,:])#tersten yazdirma
#sonuc
"""
           Ad  Yas  Maas  Boy
5  blitzcrank   28  2000  200
4       brand   27  1900  190
3        pyke   26  1800  180
2     morgana   25  1600  170
1         lux   24  1450  160
0        ashe   23  1550  150

"""

print(dataframe1.loc[:,:"Maas"])#tum satirlari, tum kolonlari sec ve aralarindan yalnizca ad, yas ve maasi cek
#sonuc
"""
           Ad  Yas  Maas
0        ashe   23  1550
1         lux   24  1450
2     morgana   25  1600
3        pyke   26  1800
4       brand   27  1900
5  blitzcrank   28  2000
"""

print(dataframe1.loc[:,"Ad"])#obje alabilen location sadece adlari verir.
print(dataframe1.iloc[:,0])#iloc ise belirttigimiz indexe sahip kolonu verir. yukaridaki ornegin bi degisik olani
#ikisinin de sonucu
"""
0          ashe
1           lux
2       morgana
3          pyke
4         brand
5    blitzcrank
"""
