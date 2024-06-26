# -*- coding: utf-8 -*-
"""Heart disease Classification Using DecisionTreeClassifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17ciqm2s54mvxX17KPaglUYngf0VH5wKD
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('/content/heart.csv')
df.head(13)

df.tail(10)

df.shape

df.info()

df.describe()

a=df['exang']
plt.plot(a)

b=df['ca']
b2=df['restecg']
plt.scatter(b,b2)

c=df['oldpeak']
plt.hist(c)

d=df['restecg']
plt.bar(d,width=100,height=100)

a3=df['exang']
plt.pie(a3)

a1=df['exang']
a2=df['restecg']
sns.lineplot(x=a1,y=a2,data=df)

b1=df['target']
b2=df['slope']
sns.scatterplot(x=b1,y=b2,data=df)

c1=df['thalach']
c2=df['ca']
sns.barplot(x=c1,y=c2,data=df)

sns.countplot(x='ca',data=df)

sns.pairplot(df,hue='ca')

a=[32,45,77,25,67,867,56]
b=[10,20,30,40,50,60,70]
sns.distplot(a,b)

df.isnull().sum()

a=df['thal']
sns.boxplot(a)

a=df.drop('target',axis=1)
a

b=df['target']
b

from sklearn.model_selection import train_test_split

a_train,a_test,b_train,b_test=train_test_split(a,b,test_size=0.30,random_state=0)

a_train.shape

a_test.shape

from sklearn.preprocessing import StandardScaler

a=StandardScaler()

X=a.fit_transform(a_train)

X

from sklearn.tree import DecisionTreeClassifier

a=DecisionTreeClassifier()
a.fit(a_train,b_train)

pre=a.predict(a_test)

from sklearn.metrics import accuracy_score

accuracy_score(pre,b_test)

from sklearn.metrics import confusion_matrix

confusion_matrix(pre,b_test)

from sklearn.tree import export_graphviz

import graphviz

graphviz.Source(export_graphviz(a,feature_names=x.columns,filled=True))