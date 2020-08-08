import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataku = pd.read_excel('data.xlsx')
print(dataku.head())
print("---")

# split dataset: 90% training & 10% test
from sklearn.model_selection import train_test_split
a, b, c, d = train_test_split(
    dataku[['ukuran', 'kamar', 'AC']],
    dataku['harga'],
    test_size = .1
)
# print(a)
# print(b)
# print(c)
# print(d)

# linear regression multi variable: multivariate linear regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# training
model.fit(a,c)

# slope/gradient (m)
print("slope/gradient")
print(model.coef_)
print("---")

# intercept (b)
print("intercept")
print(model.intercept_)
print("---")

# akurasi (score)
print("akurasi")
print(model.score(b,d) * 100, '%')
print("---")

# prediksi:
# ukuran: 60, kamar: 3, AC: 2
print(model.predict([[60, 3, 2]]))  # 605jt => 598.8jt
# ukuran: 100, kamar: 3, AC: 3 
print(model.predict([[100, 3, 3]]))  # 1005jt => 1011jt