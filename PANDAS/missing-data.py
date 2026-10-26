import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data, index = ['a','c','e','f','h'], columns =['column1','column2','column3'])

df = df.reindex(['a','b','c','d','e','f','g','h'])

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"] = newColumn

result = df
result = df.drop("column1", axis = 1) #drop:satır ya da sütun siler.axis = 1 sütun axis = 0 satır.
result = df.drop(["column1","column2"], axis = 1) 
result = df.drop('a', axis = 0) 
result = df.drop(['a','b','h'], axis = 0) 

result = df.isnull() #isnull:bir veri setindeki eksik veya tanımlanmamış (boş) değerleri tespit etmek için kullanılır.
result = df.notnull() #notnull:veri setinizdeki eksik veya boş olmayan (dolu) değerleri tespit etmek için kullanılan bir fonksiyondur.
result = df.isnull().sum()
result = df["column1"].isnull().sum() #sütun 1 deki kaç tane toplma boş değer olduğunu verir.
result = df[df["column1"].isnull()]
result = df[df["column1"].isnull()]["column1"]
result = df[df["column1"].notnull()]["column1"]

result = df.dropna() # axis = 0 yani satırları silme boş olmayan satırları getirir.(NaN, None, null) değerlerin bulunduğu satırları veya sütunları tamamen silmek için kullanılır.
result = df.dropna(axis = 1) # axis = 1 yani sütunları silme boş olmayan satırları getirir.(NaN, None, null) değerlerin bulunduğu satırları veya sütunları tamamen silmek için kullanılır.
result = df.dropna(how = "any") #any:Eğer herhangi bir sütunda NaN, None veya boş bir değer bulursa, o satırın diğer hücreleri dolu olsa bile satırı tamamen siler.
result = df.dropna(how = "all") #all:"Eğer satırın tamamı boşsa sil, ama içinde en az bir tane bile dolu hücre varsa o satıra dokunma."
result = df.dropna(subset = ["column1","column2"], how = "all")
result = df.dropna(subset = ["column1","column2"], how = "any")
result = df.dropna(thresh = 2) #"Bir satırın silinmemesi için en az 2 tane dolu (NaN olmayan) hücresi olmalı."
result = df.dropna(thresh = 3) #"Bir satırın silinmemesi için en az 3 tane dolu (NaN olmayan) hücresi olmalı."

result = df.fillna(value = 'no input') #fillna:veri setindeki eksik (NaN, None) değerleri istediğiniz bir değerle doldurmanızı sağlayan fonksiyondur.
result = df.fillna(value = '1')

result = df.sum()
result = df.sum().sum()
result = df.size #size:bir veri çerçevesindeki (DataFrame) veya serideki toplam hücre sayısını veren bir özelliktir
result = df.isnull().sum()
result = df.isnull().sum().sum()


def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size -  df.isnull().sum().sum()
    return toplam / adet
result = df.fillna(value = ortalama(df))



print(result)
