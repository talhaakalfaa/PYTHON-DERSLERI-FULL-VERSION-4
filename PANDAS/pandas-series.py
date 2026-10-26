import pandas as pd
import numpy as np

# data
numbers = [20,30,40,50]
letters = ['s','b','c','d']
dict = {'a':10,'b':20,'c':30,'d':40}
random_numbers = np.random.randint(10,100,6)


# pandas_series = pd.Series()
# pandas_series = pd.Series(numbers)
# pandas_series = pd.Series(letters)
# pandas_series = pd.Series(5, [0,1,2,3])
# pandas_series = pd.Series(numbers, ['a','b','c','d'])
# pandas_series = pd.Series(dict)
# pandas_series = pd.Series(random_numbers)

pandas_series = pd.Series([20,30,40,50], ['a','b','c','d'])

# result = pandas_series[0]
# result = pandas_series[-1]
# result = pandas_series[:2]
# result = pandas_series[-2:]
# result = pandas_series['a']
# result = pandas_series['d']
# result = pandas_series[['a','c','e']]
# result = pandas_series.ndim #ndim series'in kaç boyutlu olduğunu söyler.
# result = pandas_series.dtype #dtype verinin hangi veri tipinde saklandığını.
# result = pandas_series.shape #shape bir veri yapısının boyutlarını (satır, sütun) gösterir.
# result = pandas_series.sum() #sum value değerlerinin toplamanı verir.
# result = pandas_series.max() #max value değerleri arasında en büyük olanı verir.
# result = pandas_series.min() #min value değerleri arasında en büyük olanı verir.
# result = pandas_series + pandas_series
# result = pandas_series + 50
# result = np.sqrt(pandas_series)

# result = pandas_series >= 50
# result = pandas_series % 2 == 0



# print(pandas_series[pandas_series % 2 == 0])
# print(pandas_series)
# print(result)




opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019 = pd.Series([40,30,40,10],["astra","corsa","grandland","insignia"])

total = opel2018 + opel2019
print(total["astra"])










