# -*- coding: utf-8 -*-
"""Loan prediction using ml.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NKR5FiRutoQxINIx7T_QqYcWTLaiNCjm

**Some library**
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 
from scipy.stats import norm 
from sklearn.preprocessing import StandardScaler
from scipy import stats 
import warnings 
warnings.filterwarnings('ignore') 
# %matplotlib inline

"""**input data from the drive to google colab**"""

from google.colab import drive

drive.mount('/content/drive')

df_train = pd.read_csv('/content/drive/MyDrive/train_u6lujuX_CVtuZ9i.csv')

"""**Look at the starting five rows notice the column for loan status**"""

df_train.head(5)

"""**This code visualizes the people applying for loan who are categorized based on gender  and marriage** 

"""

grid = sns.FacetGrid(df_train, row='Gender', col='Married', size=2.2, aspect=1.6) 
grid.map(plt.hist, 'ApplicantIncome', alpha=.5, bins=10) 
grid.add_legend()

"""**Histogram and normal probability plot** 

"""

sns.distplot(df_train['ApplicantIncome'], fit=norm); 
fig = plt.figure() 
res = stats.probplot(df_train['ApplicantIncome'], plot=plt)

"""**correlation matrix**"""

corrmat = df_train.corr() 
f, ax = plt.subplots(figsize=(12, 9)) 
sns.heatmap(corrmat, vmax=.8, square=True);

""" **This graph depicts the combination of applicant income, married people and  dependent people in a family **

"""

grid = sns.FacetGrid(df_train, row='Married', col='Dependents', size=3.2, aspect=1.6) 
grid.map(plt.hist, 'ApplicantIncome', alpha=.5, bins=10) 
grid.add_legend()

""" **The graph which differentiates the applicant income distribution, Coapplicant income  distribution, loan amount distribution**

"""

flg, axes = plt.subplots(nrows = 1, ncols = 3, figsize = (14,6))
sns.distplot(df_train['ApplicantIncome'], ax = axes[0]).set_title('ApplicantIncome Distrib ution') 
sns.distplot(df_train['CoapplicantIncome'], color = "r", ax = axes[1]).set_title('Coapplican tIncome Distribution') 
axes[1].set_ylabel('CoapplicantIncome Count') 
sns.distplot(df_train['LoanAmount'],color = "g", ax = axes[2]).set_title('LoanAmount Dist ribution') 
axes[2].set_ylabel('LoanAmount Count') 
plt.tight_layout() 
plt.show() 
plt.gcf().clear()

"""**This figure shows the count of people differentiated based on education**"""

fig, axes = plt.subplots(ncols=3,figsize=(12,6)) 
g = sns.countplot(df_train["Education"], ax=axes[0]) 
plt.setp(g.get_xticklabels(), rotation=90) 
g = sns.countplot(df_train["Self_Employed"], ax=axes[1]) 
plt.setp(g.get_xticklabels(), rotation=90) 
g = sns.countplot(df_train["Property_Area"], ax=axes[2]) 
plt.setp(g.get_xticklabels(), rotation=90) 
plt.tight_layout() 
plt.show() 
plt.gcf().clear()

"""** Logistic Regression model **"""

import pandas as pd 
import numpy as np # For mathematical calculations 
import seaborn as sns # For data visualization 
import matplotlib.pyplot as plt # For plotting graphs

"""**importing data**"""

train = pd.read_csv('/content/drive/MyDrive/train_u6lujuX_CVtuZ9i.csv') 
test = pd.read_csv('/content/drive/MyDrive/test_Y3wMUE5_7gLdaTN.csv')

""" Converting the values to number"""

train['Dependents'].replace('3+', 3,inplace=True) 
test['Dependents'].replace('3+', 3,inplace=True)

""" take a look at the top 5 rows of the train set, notice the column "Loan_Status""""

train.head()

"""take a look at the top 5 rows of the test set, notice the absense of "Loan_Status" that we will predict 

"""

test.head()

""" Check How many Null Values in each columns """

train.isnull().sum()

""" Train Categorical Variables Missisng values 

"""

train['Gender'].fillna(train['Gender'].mode()[0], inplace=True) 
train ['Married'].fillna(train['Married'].mode()[0],inplace=True) 
train['Dependents'].fillna(train['Dependents'].mode()[0], inplace=True) 
train['Self_Employed'].fillna(train['Self_Employed'].mode()[0], inplace=True)
train['Credit_History'].fillna(train['Credit_History'].mode()[0], inplace=True)

"""Train Numerical Variables Missing Values"""

train['Loan_Amount_Term'].fillna(train['Loan_Amount_Term'].mode()[0], inplace=True) 
train['LoanAmount'].fillna(train['LoanAmount'].median(), inplace=True)

""" Train Check if any Null Values Exits"""

train.isnull().sum()

"""Test Check How many Null Values in each columns """

test.isnull().sum()

"""test Categorical Variables Missisng values"""

test['Gender'].fillna(test['Gender'].mode()[0], inplace=True) 
test ['Married'].fillna(test['Married'].mode()[0],inplace=True)
test['Dependents'].fillna(test['Dependents'].mode()[0], inplace=True)
test['Self_Employed'].fillna(test['Self_Employed'].mode()[0], inplace=True)
test['Credit_History'].fillna(test['Credit_History'].mode()[0], inplace=True)

""" test Numerical Variables Missing Values """

test['Loan_Amount_Term'].fillna(test['Loan_Amount_Term'].mode()[0], inplace=True) 
test['LoanAmount'].fillna(test['LoanAmount'].median(), inplace=True)

""" test Check if any Null Values Exits 

"""

test.isnull().sum()

"""Outlier treatment"""

train['LoanAmount'] = np.log(train['LoanAmount']) 
test['LoanAmount'] = np.log(test['LoanAmount'])

""" Separting the Variable into Independent and Dependent"""

X = train.iloc[:, 1:-1].values 
y = train.iloc[:, -1].values

"""Converting Categorical variables into dummy 

"""

from sklearn.preprocessing import LabelEncoder,OneHotEncoder 
labelencoder_X = LabelEncoder()

X[:,0] = labelencoder_X.fit_transform(X[:,0])

X[:,1] = labelencoder_X.fit_transform(X[:,1])

X[:,3] = labelencoder_X.fit_transform(X[:,3])

X[:,4] = labelencoder_X.fit_transform(X[:,4])

X[:,-1] = labelencoder_X.fit_transform(X[:,-1])

""" Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

""" Fitting Logistic Regression to our training set"""

from sklearn.linear_model import LogisticRegression 
classifier = LogisticRegression(random_state=0) 
classifier.fit(X_train, y_train)

""" Predecting the results"""

y_pred = classifier.predict(X_test)

""" Printing values of whether loan is accepted or rejected"""

y_pred[:100]

""" import classification_report

"""

from sklearn.metrics import classification_report 
print(classification_report(y_test, y_pred))

"""implementing the confusion matrix """

from sklearn.metrics import confusion_matrix 
cm = confusion_matrix(y_test, y_pred) 
print(cm)

sns.heatmap(cm, annot=True, fmt="d") 
plt.title('Confusion matrix of the classifier') 
plt.xlabel('Predicted') 
plt.ylabel('True')

"""Check Accuracy"""

from sklearn.metrics import accuracy_score 
accuracy_score(y_test,y_pred)

""" Applying k-Fold Cross Validation"""

from sklearn.model_selection import cross_val_score 
accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10) 
accuracies.mean()