# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 19:33:23 2022

@author: dcaos
"""

import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns 
from sklearn.linear_model import LinearRegression, LogisticRegression 

# Regression Practice 

# Load Data set 
data = pd.read_csv("C:/Users/dcaos/NotebookStuff/heightByGenderDataset.csv")
gamesData = pd.read_csv("C:/Users/dcaos/NotebookStuff/archive/games_of_all_time.csv")

print(data.head())
print(gamesData.head())

#X = data["Male Height in Ft"].array.reshape(-1,1)
#y = data["Female Height in Ft"].array.reshape(-1,1)

#ind = gamesData[["meta_score","user_score"]]
dep = gamesData[["user_score"]]
ind = pd.get_dummies(gamesData,columns=["platform"])
#ind = gamesData[["meta_score"]]
ind = ind.drop(["game_name","description","developer","genre","type","url","rating"],axis = 1)
#ind = gamesData.drop(["user_score"],axis = 1)
#dep = dep.to_numpy().reshape(-1,1)
#dep = dep.values.ravel()


#lr = LinearRegression().fit(X,y)
#LogReg = LogisticRegression().fit(ind,dep)
LinReg = LinearRegression().fit(ind,dep)


gamesData.corr()
sns.heatmap(gamesData.corr())


x = ind
y = dep



lr.score(X,y)
print(lr.score(X,y))
print(lr.coef_)
print(lr.intercept_)



