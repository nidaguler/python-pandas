import pandas as pd

dictionary={"Ad":["Zed","Yasuo","Malphite","Garen","Zilean","Gangplank"],
            "Yas":[21,22,23,24,25,26],
            "Maas":[1500,1600,1700,1800,1900,2000],
            "Boy":[160,170,180,190,200,210]}
dataframe1=pd.DataFrame(dictionary)

dataframe1["yepyeni_kolon"]=[each*2 for each in dataframe1.Yas]#list comprehension ile yeni kolon ekliyoruz
#bu kolona yaslari 2 ile carpip ekliyoruz.
#sonuc
"""
          Ad  Yas  Maas  Boy  yepyeni_kolon
0        Zed   21  1500  160             42
1      Yasuo   22  1600  170             44
2   Malphite   23  1700  180             46
3      Garen   24  1800  190             48
4     Zilean   25  1900  200             50
5  Gangplank   26  2000  210             52
"""
#apply metodu ile de ayni islemi yapabiliriz.
#bi fonksiyon olusturalim
def multiply(Yas):
    return Yas*2

dataframe1["list comp"]=dataframe1.Yas.apply(multiply)
#sonuc
"""
          Ad  Yas  Maas  Boy  yepyeni_kolon  list comp
0        Zed   21  1500  160             42         42
1      Yasuo   22  1600  170             44         44
2   Malphite   23  1700  180             46         46
3      Garen   24  1800  190             48         48
4     Zilean   25  1900  200             50         50
5  Gangplank   26  2000  210             52         52

"""