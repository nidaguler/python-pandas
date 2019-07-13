"""
Neden Pandas kullanmaliyiz?
1) dataframeler icin pandas hizli ve etkili.
2) dosyalar arasi gecis kolaydir.
3) NaN value olabilir
4) reshape yapıp datayı etkili bir sekilde kullanabiliriz.
5) slicing ve indexing kolay
6) time series data analizinde cok yardimci olur
7) hiz acisindan optimize edilmis hizli bir kutuphane
"""

import pandas as pd #pandası import edelim.

dictionary= {"Ad":["ashe","lux","morgana","pyke","brand","blitzcrank"],
             "Yas":[23,24,25,26,27,28],
             "Maas":[1550,1450,1600,1800,1900,2000]}
dataframe1=pd.DataFrame(dictionary) 
"""
pd.DataFrame yazarak dataframemimizi olusturuyoruz. spyderda sağ tarafta variable explorerden dataframe1e
tıkladıgınızda karsınıza excel gorunumlu bi ekran gelmis olacak
"""
head=dataframe1.head()#bu head metodu bize ilk 5 indexi verir dataframedeki
tail=dataframe1.tail()#tail metodu son 5 indexi verir.
