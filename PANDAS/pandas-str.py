import pandas as pd

data = pd.read_csv("nba.csv")

data.dropna(inplace = True)

# data["Name"] = data["Name"].str.upper() #name kolonundaki bütün hafrleri büyük yapar
# data["Name"] = data["Name"].str.lower() #name kolonundaki bütün hafrleri küçük yapar
# data["İndex"] = data["Name"].str.find('a') #name kolonundaki 'a' harflerinin indeksini bulur.
# data = data[data.Name.str.contains('Jordan')] #contains:metin (string) verileri içerisinde belirli bir kelimeyi, harfi veya karakter dizisini aramak için kullanılır.
# data = data.Team.str.replace(' ','-')
data[['FirstName','LastName']] = data['Name'].loc[data['Name'].str.split().str.len()==2].str.split(expand = True)


print(data.head(10))