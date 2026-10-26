import pandas as pd

# customers = {
#     'CustomerId': [1,2,3,4],
#     'FirstName': ["talha","çağan","selin","ilknur"],
#     'LastName': ["kalfa","kalfa","oğuz","özdemir"]
# }

# orders = {
#     'OrderId': [10,11,12,13],
#     'CustomerId': [1,2,5,7],
#     'OrderDate': ['2010-07-04','2010-07-07','2012-07-04','2012-07-04']
# }

# df_customers = pd.DataFrame(customers, columns = ["CustomerId","FirstName","LastName"])
# df_orders = pd.DataFrame(orders, columns = ["OrderId","CustomerId","OrderDate"])

# print(df_customers)
# print(df_orders)

# result = pd.merge(df_customers,df_orders,how = "inner") #merge:iki farklı tabloyu (DataFrame) ortak bir sütun veya anahtar üzerinden birleştirmek için kullanılır.
# #inner:kesişim kümesini alacağını ifade eder.
# result = pd.merge(df_customers,df_orders,how = "left") #left:Bu yöntemde, ilk tablodaki tüm satırlar korunur. ikinci tablodan ise sadece ilk tablodaki kayıtlarla eşleşen veriler getirilir. Eğer ilk tablodaki bir kaydın ikinci tabloda karşılığı yoksa, o kısımlar NaN (boş) olarak görünür.
# result = pd.merge(df_customers,df_orders,how = "right") #right:ikinci tablodaki tüm satırlar korunur; ilk tablodan ise sadece ikinci tabloyla eşleşenler getirilir. Eğer ikinci bir kaydın ilkde karşılığı yoksa, ilk taraftan gelecek bilgiler NaN (boş) olarak doldurulur.
# result = pd.merge(df_customers,df_orders,how = "outer") #outer:tüm satırları bir araya getirir. Kısacası, hiçbir veriyi kaybetmek istemediğinizde kullanılır. Eğer bir kayıt bir tabloda var ama diğerinde yoksa, eksik olan kısımları NaN (boş) ile doldurur.

customersA = {
    'CustomerId': [1,2,3,4],
    'FirstName': ["talha","çağan","selin","ilknur"],
    'LastName': ["kalfa","kalfa","oğuz","özdemir"]
}

customersB = {
    'CustomerId': [4,5,6,7],
    'FirstName': ["ezel","ali","eyşan","azad"],
    'LastName': ["bayraktar","kırgız","atay","kırgız"]
}


df_customersA = pd.DataFrame(customersA, columns = ["CustomerId","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB, columns = ["CustomerId","FirstName","LastName"])

result = pd.concat([df_customersA,df_customersB]) #concat:iki veya daha fazla tabloyu bir trenin vagonları gibi uç uca eklemek veya yan yana yapıştırmak için kullanılır.
result = pd.concat([df_customersA,df_customersB],axis = 1) #axis = 1 yazarsan yan yana birleştirir
result = pd.concat([df_customersA,df_customersB],axis = 0) #axis = 0 yazarsan alt alta birleştirir = result = pd.concat([df_customersA,df_customersB])

print(result)