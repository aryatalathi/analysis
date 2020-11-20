# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 09:57:05 2020

@author: aryat
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
import re
import sys

df=pd.read_csv('E:/skill based activity/Yoga.csv',encoding='cp1252')
print(df)
print(df.dtypes)
print(df.describe())

replaces = [u'\u00AE', u'\u2013', u'\u00C3', u'\u00E3', u'\u00B3', '[', ']', "'"]
for i in replaces:
    df['For how many hours you have to work and use laptop/phone? (put  No if not applicable)'] = df['For how many hours you have to work and use laptop/phone? (put  No if not applicable)'].astype(str).apply(lambda x : x.replace(i, ''))

regex = [r'[+|/:/;(_)@]', r'\s+', r'[A-Za-z]+']
for j in regex:
    df['For how many hours you have to work and use laptop/phone? (put  No if not applicable)'] = df['For how many hours you have to work and use laptop/phone? (put  No if not applicable)'].astype(str).apply(lambda x : re.sub(j, '', x))

print(df['For how many hours you have to work and use laptop/phone? (put  No if not applicable)'])

from sklearn.preprocessing import LabelEncoder

df1 = df.copy(deep = True)
le_color = LabelEncoder()
df1['Are you practicing yoga/meditation everyday?'] = le_color.fit_transform(df['Are you practicing yoga/meditation everyday?'])

le_genre = LabelEncoder()
df1['Is practicing yoga/meditation necessary?'] = le_genre.fit_transform(df['Is practicing yoga/meditation necessary?'])


le_beverage = LabelEncoder()
df1['Are you working from office/home or attending online lectures?'] = le_beverage.fit_transform(df['Are you working from office/home or attending online lectures?'])


le_drink = LabelEncoder()
df1['Do you feel stressed due to work load?'] = le_drink.fit_transform(df['Do you feel stressed due to work load?'])


print(df1)
w = sns.countplot(
    data=df,
    x="Age", y=None)
plt.show()
x = sns.countplot(
    data=df,
    x="Are you practicing yoga/meditation everyday?", y=None)
plt.show()
y = sns.countplot(
    data=df,
    x="Do you feel stressed due to work load?", y=None)
plt.show()
z = sns.countplot(
    data=df,
    x="Are you working from office/home or attending online lectures?", y=None)
plt.show()


df.to_csv('E:/skill based activity/12345.csv')