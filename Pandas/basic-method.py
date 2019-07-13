import pandas as pd

dictionary= {"Ad":["ashe","lux","morgana","pyke","brand","blitzcrank"],
             "Yas":[23,24,25,26,27,28],
             "Maas":[1550,1450,1600,1800,1900,2000]}

dataframe1=pd.DataFrame(dictionary)

print(dataframe1.columns)#dataframedeki kolonlari verir.
#sonuc
"""
Index(['Ad', 'Yas', 'Maas'], dtype='object')
"""
print(dataframe1.info())
#sonuc
"""
<class 'pandas.core.frame.DataFrame'> #pandas dataframei oldugu hakkında bilgi
RangeIndex: 6 entries, 0 to 5 #rangeindex index sayisi, indexlerin 0-5 arasinda oldugunu belirtiyor
Data columns (total 3 columns): #3 tane kolonun var diyor bunlar; ad,yas,maas
Ad      6 non-null object #6 tane bos olmayan obje var diyor.pandasta obje=string
Yas     6 non-null int64 #6 bos olmayan tane yas degeri var bunlar integer 
Maas    6 non-null int64 #6 bos olmayan tane maas degeri var bunlar integer
dtypes: int64(2), object(1) # data tipi olarak 2 integer 1 obje var
memory usage: 224.0+ bytes #hafiza kullanimi 224 byte
None
"""

print(dataframe1.dtypes)#her kolonun data typeini verir.
#sonuc
"""
Ad      object
Yas      int64
Maas     int64
"""
print(dataframe1.describe())#numeric feature = kolonlar =yas,maas
#sonuc
"""
             Yas         Maas
count   6.000000     6.000000 #6 adet yas ve maas var
mean   25.500000  1716.666667 #dataframedeki tum yaslarin ortalamasi= 25.5 ve maaslarin ortalamasi= 1716.666667
std     1.870829   216.024690 #
min    23.000000  1450.000000 #minimum yas= 23, minimum maas=1450
25%    24.250000  1562.500000 #
50%    25.500000  1700.000000 #
75%    26.750000  1875.000000 #
max    28.000000  2000.000000 #maximum yas=28, maximum maas=2000
"""
