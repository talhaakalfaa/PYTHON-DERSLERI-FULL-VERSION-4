import pandas as pd
import numpy as np
personeller = {
    'Çalışan': ['talha kalfa','selin oğuz','ilknur özdemir','çağan kalfa','nurettin kalfa','osman cem eren'],
    'Departman': ['insan kaynakları','bilgi işlem','muhasabe','insan kaynakları','pazarlama','pazarlama'],
    'Yaş': [19,19,50,28,57,29],
    'Semt': ['kadıköy','tuzla','maltepe','tuzla','maltepe','kadıköy'],
    'Maaş': [5000,3000,4000,3500,2750,6500]
}

df = pd.DataFrame(personeller)

result = df

result = df["Maaş"].sum()
result = df.groupby("Departman").groups # groups departman içinde gruplama yapar.departman yerine herşey olur.
result = df.groupby(["Departman","Semt"]).groups


# for name, group in df.groupby("Semt"):
#     print(name)
#     print(group)


# for name, group in df.groupby("Departman"):
#     print(name)
#     print(group)

result = df.groupby("Semt").get_group("tuzla") # get_group:sütun içinde arama yapar. 
result = df.groupby("Departman").get_group("pazarlama") # get_group:sütun içinde arama yapar. 
result = df.groupby("Departman").sum()
result = df.groupby("Departman")["Maaş"].mean() #maaş ortalaması alır. MEAN ortalama al demek.
result = df.groupby("Departman")[["Yaş","Maaş"]].mean()
result = df.groupby("Semt")["Yaş"].mean()
result = df.groupby("Semt")["Maaş"].mean()
result = df.groupby("Semt")["Çalışan"].count() #count:Bir liste içindeki belirli bir elemanın kaç kez tekrarlandığını sayar.
result = df.groupby("Departman")["Yaş"].max()
result = df.groupby("Departman")["Maaş"].min()
result = df.groupby("Departman")["Maaş"].max()["muhasabe"] #muhasabeye dışarı yazınca sadece departman içinden muhasabe içinde max alınan maşa bakar.
result = df.groupby("Departman")["Maaş"].agg(np.mean) #agg:birden fazla işlem yapar toplama gibi...
result = df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]).loc["pazarlama"]

print(result)
