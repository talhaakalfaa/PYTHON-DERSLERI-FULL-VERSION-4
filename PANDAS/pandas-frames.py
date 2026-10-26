import pandas as pd

list = [["Selin",50],["Talha",60],["Çağan",70],["İlknur",80]]
dict = {"Name":["selin","talha","çağan","ilknur"], "grade": [50,60,70,80]}
dict_list = [
                {"Name":"selin","grade":50},
                {"Name":"talha","grade":60},
                {"Name":"çağan","grade":70},
                {"Name":"ilknur","grade":80}
                ]

# df = pd.DataFrame()
# df = pd.DataFrame([1,2,3,4])
# df = pd.DataFrame(data, index = [1,2,3,4], columns = ['İsim','Not'])
# df = pd.DataFrame(dict)
# df = pd.DataFrame(dict, index = ["212","232","236","456"])
# df = pd.DataFrame(dict_list)
df = pd.DataFrame(dict_list, index = ["212","232","236","456"])


print(df)








# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1 , oranges = s2)

# df = pd.DataFrame(data)

# print(df)


