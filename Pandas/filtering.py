import pandas as pd

dictionary={"Ad":["Zed","Yasuo","Malphite","Garen","Zilean"],
            "Yas":[21,22,23,24,25],
            "Maas":[1500,1600,1700,1800,1900],
            "Boy":[160,170,180,190,200]}
dataframe1=pd.DataFrame(dictionary)
#filtering islemlerinde istedigimiz araliktaki verileri cekebiliyoruz.

#-----------------------------------------------------------------------------
filter1=dataframe1.Boy <180 #boyu 180 cmden asagida olanlari bize yazdiracak.
print(filter1)
#sonuc
"""
0     True -> 160
1     True -> 170
2    False -> 180
3    False -> 190
4    False -> 200
"""
filtrelenmis_data=dataframe1[filter1]
print(filtrelenmis_data)
#sonuc
"""
      Ad  Yas  Maas  Boy
0    Zed   21  1500  160
1  Yasuo   22  1600  170
"""
#----------------------------------------------------------------------------
#simdi hem boyu 180cmden kısa olanlari ve maasi 1500den fazla olanlari bulalim

filter2=dataframe1.Maas > 1500
#simdi ustteki filter1 ile birlestirip ikisini de isleme sokalim
ikifilterli_data=dataframe1[filter1 & filter2] # & isareti filtreleri birlestirmeye yarar ve anlamindadir
print(ikifilterli_data)
#sonuc
"""
      Ad  Yas  Maas  Boy
1  Yasuo   22  1600  170
"""
#dataframeden sectigimiz herhangi  birini bulalim. ben gareni buldurmak istiyorum.
filter3=dataframe1.Boy == 190
filter4=dataframe1.Maas == 1800
filtrelenmis_data2=dataframe1[filter3 & filter4]
print(filtrelenmis_data2)
#sonuc
"""
      Ad  Yas  Maas  Boy
3  Garen   24  1800  190
"""
