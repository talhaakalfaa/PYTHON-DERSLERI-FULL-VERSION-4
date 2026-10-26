import pandas as pd
df = pd.read_csv("IMDB_Bottom250movies2_OMDB_Detailed.csv")

# 1- dosyada hakkındaki bilgiler.
result = df
# 2- ilk 5 kaydı gösterin.
result = df.head()
# 3- ilk 10 kaydı gösterin.
result = df.head(10)
# 4- son 5 kaydı gösterin.
result = df.tail()
# 5- son 10 kaydı gösterin.
result = df.tail(10)
# 6- sadece Movie_title kolonunu alın.
result = df["Title"]
# 7- sadece Movie_title kolonunu içeren ilk 5 kaydı alınız.
result = df["Title"].head()
# 8- sadece Movie_title ve rating kolonunu içeren ilk 5 kaydı alınız.
result = df[["Title","Year"]].head()
# 9- sadece Movie_title ve rating kolonunu içeren son 7 kaydı alınız.
result = df[["Title","Year"]].tail(7)
# 10- sadecce Movie_title ve rating kolonunu içeren ikinci 5 kaydı alınız.
result = df[5:][["Title","Year"]].head(5)
# 11- sadece Movie_title ve rating kolonunu içeren ve imbd puanı 8.0
#     ve üstünde olan kayıtlardan ilk 50 tanesini alınız.
result = df[df["Year"] >= 2000][["Title","Year"]].head(50)
# 12- yayın tarihi 2014 ile 2015 arasında olan filmerin isimlerini getiriniz.
result = df[(df["Year"] >= 2014) & (df["Year"] <= 2015)][["Title","Year"]]
# 13- değerlendirme sayısı (Num_Reviews) 100.000 den büyük ya da imbd puanı 
#     8 ile 9 arasında olan filmleri listeleyiniz. 
result = df



print(result)