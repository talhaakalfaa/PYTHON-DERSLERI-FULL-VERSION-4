import pandas as pd

df = pd.read_csv("GBvideos.csv")


# 1- İlk 10 kaydı getiriniz.
result = df.head(10)
# 2- İkinci 5 kaydı getiriniz
result = df[5:20].head(5)
# 3- Dataset' de bulunun kolan isimlerini ve sayısını bulunuz.
result = df.columns
result = len(df.columns)
# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyeniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_erros_or_removed,description)
df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"], axis = 1, inplace = True)
result = df
# 5- beğenme(likes) ve beğenmeme(dislikes) sayılarının ortalamasını bulunuz.
result = df["likes"].mean()
result = df["dislikes"].mean()
# 6- ilk 50 likes ve dislikes kolonlarını getiriniz.
result = df[["likes","dislikes"]].head(50)
# 7- en çok görüntülenen video hangisidir ?
result = df[df["views"].max() == df["views"]]["title"].iloc[0]
# 8- en düşük görüntülenen video hangisidir ?
result = df[df["views"].min() == df["views"]]["title"].iloc[0]
# 9- en fazla görüntülenen ilk 10 video hangisidir ?
result = df.sort_values("views", ascending=False).head(10)[["title","views"]]
# 10- Kategoriye göre beğeni ortalamarını sıralı şekilde getiriniz.
result = df.groupby("category_id")["likes"].mean().sort_values()
# 11- kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
result = df.groupby("category_id")["comment_count"].mean().sort_values()
# 12- her kategoride kaç video vardır ?
result = df["category_id"].value_counts()
# 13- her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz
df["title_len"] = df["title"].apply(len)
result = df
# 14- her video için kullanılan tag sayısını yeni kolonda gösteriniz
df["tag_count"] = df["tags"].apply(lambda x: len(x.split('|')))
# 15- en popüler videoları listeleyiniz.(like/dislike oranına göre)

likesList = list(df["likes"])
dislikesList = list(df["dislikes"])

def likedislikeoranhesapla(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])

    liste = list(zip(likesList,dislikesList))  # (1020,230), (201,233)

    oranListesi = []

    for like, dislike in liste:
        if (like + dislike) == 0:
            oranListesi.append(0)
        else:
            oranListesi.append(like/(like+dislike))

    return oranListesi

df["beğeni_orani"] = likedislikeoranhesapla(df)

print(df.sort_values("beğeni_orani", ascending=False)[["title","likes","dislikes","beğeni_orani"]])







