import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns = ["Column1","Column2","Column3","Column4","Column5"])
#***SORGULAMA***#
result = df
result = df.columns
result = df.head() #HEAD:DataFrame en üstündeki satırları görmeni sağlar.(ilk 5)
result = df.head(10) #ilk 10 satır
result = df.tail() #TAİL:DataFrame en sonundaki satırları görmeni sağlar.(son 5)
result = df.tail(10) #son 10 satır
# result = df["Column1"].head()
# result = df.Column1.head() = result = df["Column1"].head()
result = df[["Column1","Column2"]].head()
result = df[["Column1","Column2"]].tail()
result = df[5:15][["Column1","Column2"]].head()
result = df[5:15][["Column1","Column2"]].tail()

#***FİLTRELEME***#
result = df > 50
result = df[df > 50]
result = df[df % 2 == 0]
result = df[df["Column1"] > 50][["Column1","Column2"]]
result = df[(df["Column1"] > 50) & (df["Column1"] <= 70)][["Column1","Column2"]]
result = df[(df["Column1"] > 50) & (df["Column2"] <= 70)]
result = df[(df["Column1"] > 50) | (df["Column2"] > 50)] # | = or demek
result = df.query("Column1 >= 50 & Column1 % 2 ==0")[["Column1","Column2"]] #query:karmaşık filtreleme işlemlerini çok daha temiz ve "insan diline yakın" bir şekilde yazmanı sağlar.
result = df.query("Column1 >= 50 | Column1 % 2 ==0")[["Column1","Column2"]] #query:karmaşık filtreleme işlemlerini çok daha temiz ve "insan diline yakın" bir şekilde yazmanı sağlar.



print(result)