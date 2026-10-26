import pandas as pd
import numpy as np

data = {
    "column1": [1,2,3,4,5],
    "column2": [10,13,20,45,25],
    "column3": ["abc","bcaa","ade","cb","dea"]
}

df = pd.DataFrame(data)

def kareal(x):
    return x * x

kareal2 = lambda x: x* x

result = df
result = df["column2"].unique() #unique:tekrar edenleri silen ve her birinden sadece birer tane bırakır ve liste verir.
result = df["column2"].nunique() #nunique:Bir sütundaki benzersiz (eşsiz) değerlerin sayısını veren fonksiyondur.
result = df["column2"].value_counts() #value_counts:Bir sütundaki her bir benzersiz değerin kaç kez tekrarlandığını sayan fonksiyondur. Verinin "çetelesini" tutar.
result = df["column1"] * 2
result = df["column1"].apply(kareal) #apply:bir sütuna veya satıra, belirli bir fonksiyonu toplu halde uygulama komutudur.
result = df["column1"].apply(kareal2)
df["column4"] = df["column3"].apply(len)
result = len(df.columns) #len bir şeyin kaç tane olduğunu bulmaya çalışır.
result = df.index
result = len(df.index)
result = df.info

result = df.sort_values("column2") #sort_values:Veri setindeki satırları, belirlediğin bir veya birden fazla sütuna göre sıralamaya yarar. Sayıları küçükten büyüğe, metinleri ise A'dan Z'ye (veya tam tersi) dizmek için kullanılır.
result = df.sort_values("column3")
result = df.sort_values("column3", ascending = False)

data = {
    "ay": ["mayıs","haziran","nisan","mayıs","haziran","nisan","mayıs","haziran","nisan"],
    "kategori": ["elektronik","elektronik","elektronik","kitap","kitap","kitap","giyim","giyim","giyim"],
    "gelir": [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data)

df = df.pivot_table(index = "ay" ,columns= "kategori", values= "gelir")
#pivot_table:Karmaşık ve büyük bir tabloyu özetleyerek, verileri daha anlamlı bir "özet tablo" haline getirmeye yarar.
print(df)